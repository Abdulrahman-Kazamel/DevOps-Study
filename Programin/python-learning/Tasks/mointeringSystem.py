import psutil

cpu_usage = psutil.cpu_percent(1)
memory_usage = psutil.virtual_memory().percent


# print(memory_usage)

if memory_usage >= 80:
    memory_usage_message = f"memory usage is high: {memory_usage}"
    print(memory_usage_message)

if cpu_usage >= 70:
    cpu_usage_message = f"cpu usage is high: {cpu_usage}"
    print(cpu_usage_message)
else:
    print(f"""none of cpu or mem is high,current values are:
        memory usage is {memory_usage} \n\tcpu usage is {cpu_usage}""")
