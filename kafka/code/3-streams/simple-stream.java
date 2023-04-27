import org.apache.kafka.streams.StreamsBuilder
import org.apache.kafka.streams.kstream.JoinWindows
import org.apache.kafka.streams.kstream.{KStream, KTable}
import org.apache.kafka.streams.scala.ImplicitConversions._
import org.apache.kafka.streams.scala.Serdes._
import org.apache.kafka.streams.scala.StreamsBuilder
import org.apache.kafka.streams.scala.kstream._

object TransactionThreshold {
  def main(args: Array[String]): Unit = {
    val builder = new StreamsBuilder()
    
    val bankTransactions: KStream[String, BankTransaction] = builder.stream[String, BankTransaction]("bank-transactions")
    val userSettings: KTable[String, UserSettings] = builder.table[String, UserSettings]("user-settings")
    
    val transactionThreshold: KStream[String, BankTransaction] = bankTransactions
      .leftJoin(userSettings,
        (transaction: BankTransaction, settings: UserSettings) => {
          if (settings != null && settings.amount >= transaction.amount) {
            transaction
          } else {
            null
          }
        })
      .filter((_, transaction) => transaction != null)
    
    transactionThreshold.to("transaction_threshold")
    
    val streams = new KafkaStreams(builder.build(), props)
    streams.start()
  }
}

case class BankTransaction(userId: String, transId: String, amount: Double)
case class UserSettings(userId: String, amount: Double)
