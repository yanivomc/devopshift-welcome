
import os
import sys
from python_terraform import Terraform



def execute_terraform(tf_content, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write(tf_content)
    print(f"✅ Terraform config written to {output_path}")

    tf = Terraform(working_dir=os.path.dirname(output_path))


    # ---- terraform init ----
    print("\n🔧 Running: terraform init")
    code, _, init_err  = tf.init(capture_output=False)
    if code != 0:
        print("❌ Init failed:\n", init_err)
        sys.exit(1)


    # ---- terraform plan ----
    print("\n📝 Running: terraform plan")
    code, plan_out, plan_err = tf.plan(capture_output=True)

    if code != 0 and "No changes" not in plan_out and "+" not in plan_out:
        print("❌ Plan failed!")
        print("STDOUT:\n", plan_out)
        print("STDERR:\n", plan_err)
        sys.exit(1)
    else:
        print("✅ Plan succeeded.\n", plan_out)



      # ---- terraform apply ----
    print("\n🚀 Running: terraform apply")
    code, apply_out, apply_err = tf.apply(skip_plan=True, capture_output=True)
    if code != 0:
        print("❌ Apply failed!")
        print("STDOUT:\n", apply_out)
        print("STDERR:\n", apply_err)
        sys.exit(1)
    print("✅ Apply succeeded.\n", apply_out)


    # ---- terraform output ----
    print("\n📤 Fetching Terraform outputs")
    code, tf_outputs, output_err = tf.output()
    if code == 0:
        for key, val in tf_outputs.items():
            print(f"{key}: {val['value']}")
    else:
        print("⚠️ Failed to fetch outputs:\n", output_err)






