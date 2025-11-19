import subprocess

model_path = r"D:\teaching\AI\tasks\task17\diffusion_project_v_evgen\models\stable-diffusion-v1-5-pruned-emaonly-f32.gguf"
sd_path = r"D:\teaching\AI\tasks\task17\diffusion_project_v_evgen\stable-diffusion.cpp\build\bin\Release\sd.exe"
prompt =r"prompt.txt"
output = "Result.png"

with open(prompt, "r") as f:
    prompt = f.read().strip()

main =[
    sd_path,
    "--model", model_path,
    "--prompt", prompt,
    "--output", output,
    "--width", "512",
    "--height", "512",
    "--steps", "30",
    "--seed", "42",
    ]
subprocess.run(main)
print(output)

