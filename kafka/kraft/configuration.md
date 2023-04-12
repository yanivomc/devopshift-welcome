# Main Kafka server configuration related to KRaft mode:

- inter.broker.listener.name: This property specifies the network interface and port to use for inter-broker communication in the KRaft cluster. By default, this is set to PLAINTEXT.

- num.network.threads: This property specifies the number of threads to use for handling network connections in the KRaft cluster. The default value is 3.

- num.io.threads: This property specifies the number of threads to use for handling I/O operations in the KRaft cluster. The default value is 8.

- group.initial.rebalance.delay.ms: This property specifies the delay (in milliseconds) before the initial consumer group rebalance occurs. The default value is 3000.

- transaction.state.log.replication.factor: This property specifies the replication factor for the - transaction state log topic used by transactional producers and consumers in the KRaft cluster. The default value is 3.

- transaction.state.log.min.isr: This property specifies the minimum number of in-sync replicas (ISRs) required for the transaction state log topic. The default value is 2.

- transaction.state.log.topic: This property specifies the name of the transaction state log topic. The default value is _txn_state.

- transaction.state.log.segment.bytes: This property specifies the segment size (in bytes) for the transaction state log topic. The default value is 10485760 (10 MB).

- transaction.state.log.cleanup.policy: This property specifies the retention policy for the transaction state log topic. The default value is delete.
