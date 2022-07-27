import matplotlib.pyplot as plt

f = open("logs.txt", "r")
data = f.read()
data = eval(data)
# print(data)

# Used Memory Plot
# usedMemory = data['used']
# names = ['Total']
# for i in range(len(usedMemory)):
#     names.append(f"used {i+1}")
#
# usedMemory.insert(0, data['total'][0])
# plt.bar(names,usedMemory)
# plt.title("Used Memory plot")
# plt.savefig("used_memory_graph.png")

# Total Memory Plot
# totalMemory = data['total']
# totalUsedMemory = data['used']
# totalAvaliableMemory = data['available']
# totalFreeMemory = data['free']
# totalActiveMemory = data['active']
# totalMemoryNames = ['Total', 'Used', 'Avaliable', 'Free', 'Active']
# totalMemoryValues = [totalMemory[len(totalMemory)-1],
#                      totalUsedMemory[len(totalUsedMemory) - 1],
#                      totalAvaliableMemory[len(totalAvaliableMemory)-1],
#                      totalFreeMemory[len(totalFreeMemory)-1],
#                      totalActiveMemory[len(totalActiveMemory) - 1]]
# plt.bar(totalMemoryNames, totalMemoryValues)
# plt.title("Total Memory plot")
# plt.savefig("total_memory_plot.png")

# Total Disk Usage
# totalDisk = data['totalDisk']
# usedDisk = data['usedDisk']
# freeDisk = data['freeDisk']
#
# totalDiskNames = ['Total Disk', 'Used Disk', 'Free Disk']
# totalDiskValues = [totalDisk[len(totalDisk)-1],
#                    usedDisk[len(usedDisk)-1],
#                    freeDisk[len(freeDisk)-1]]
# plt.bar(totalDiskNames, totalDiskValues)
# plt.title("Total Disk plot")
# plt.savefig("total_disk_plot.png")

# Total CPU usage
total_cpu = data['cpu']
cpu_names = ['CPU 1', 'CPU 2', 'CPU 3', 'CPU 4']
for i in range(len(total_cpu)):
    cpu_values = [f"{total_cpu[i][0]}", f"{total_cpu[i][1]}", f"{total_cpu[i][2]}", f"{total_cpu[i][3]}"]
    # plt.bar(cpu_names, cpu_values)
    plt.title("Total CPU plot")
    colors = ['green', 'brown', 'blue', 'red']
    plt.pie(cpu_values, labels=cpu_names, colors=colors)
    plt.axis('equal')
    plt.savefig(f"total_cpu_plot{i}.png")
    plt.close()
# # Plot some numbers:

# # plt.plot(names, values)
# plt.bar(names, values)
# # plt.scatter(names, values)
# #
# # colors = ['green', 'brown', 'blue', 'red']
# # plt.pie(values, labels=names, colors=colors)
# # plt.axis('equal')

#
