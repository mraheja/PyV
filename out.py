import time
import json
time_dict, prev_time = {}, time.time()
f_time = open('time.json','w')
import torch
time_dict[0] = time_dict.get(0,0) + time.time() - prev_time
prev_time = time.time()
import torch.nn as nn
time_dict[1] = time_dict.get(1,0) + time.time() - prev_time
prev_time = time.time()
import torch.nn.functional as F
time_dict[2] = time_dict.get(2,0) + time.time() - prev_time
prev_time = time.time()
class Net(nn.Module):
    def __init__(self):
        global prev_time
        time_dict[7] = time_dict.get(7,0) + time.time() - prev_time
        prev_time = time.time()
        super(Net, self).__init__()
        time_dict[8] = time_dict.get(8,0) + time.time() - prev_time
        prev_time = time.time()
        # 1 input image channel, 6 output channels, 5x5 square convolution
        time_dict[9] = time_dict.get(9,0) + time.time() - prev_time
        prev_time = time.time()
        # kernel
        time_dict[10] = time_dict.get(10,0) + time.time() - prev_time
        prev_time = time.time()
        self.conv1 = nn.Conv2d(1, 6, 5)
        time_dict[11] = time_dict.get(11,0) + time.time() - prev_time
        prev_time = time.time()
        self.conv2 = nn.Conv2d(6, 16, 5)
        time_dict[12] = time_dict.get(12,0) + time.time() - prev_time
        prev_time = time.time()
        # an affine operation: y = Wx + b
        time_dict[13] = time_dict.get(13,0) + time.time() - prev_time
        prev_time = time.time()
        self.fc1 = nn.Linear(16 * 5 * 5, 12000)  # 5*5 from image dimension
        time_dict[14] = time_dict.get(14,0) + time.time() - prev_time
        prev_time = time.time()
        self.fc2 = nn.Linear(12000, 84)
        time_dict[15] = time_dict.get(15,0) + time.time() - prev_time
        prev_time = time.time()
        self.fc3 = nn.Linear(84, 10)
        time_dict[16] = time_dict.get(16,0) + time.time() - prev_time
        prev_time = time.time()
    def forward(self, x):
        global prev_time
        time_dict[18] = time_dict.get(18,0) + time.time() - prev_time
        prev_time = time.time()
        # Max pooling over a (2, 2) window
        time_dict[19] = time_dict.get(19,0) + time.time() - prev_time
        prev_time = time.time()
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        time_dict[20] = time_dict.get(20,0) + time.time() - prev_time
        prev_time = time.time()
        # If the size is a square, you can specify with a single number
        time_dict[21] = time_dict.get(21,0) + time.time() - prev_time
        prev_time = time.time()
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        time_dict[22] = time_dict.get(22,0) + time.time() - prev_time
        prev_time = time.time()
        x = torch.flatten(x, 1) # flatten all dimensions except the batch dimension
        time_dict[23] = time_dict.get(23,0) + time.time() - prev_time
        prev_time = time.time()
        x = F.relu(self.fc1(x))
        time_dict[24] = time_dict.get(24,0) + time.time() - prev_time
        prev_time = time.time()
        x = F.relu(self.fc2(x))
        time_dict[25] = time_dict.get(25,0) + time.time() - prev_time
        prev_time = time.time()
        x = self.fc3(x)
        time_dict[26] = time_dict.get(26,0) + time.time() - prev_time
        prev_time = time.time()
        return x
        time_dict[27] = time_dict.get(27,0) + time.time() - prev_time
        prev_time = time.time()
net = Net()
time_dict[30] = time_dict.get(30,0) + time.time() - prev_time
prev_time = time.time()
params = list(net.parameters())
time_dict[32] = time_dict.get(32,0) + time.time() - prev_time
prev_time = time.time()
saved = []
time_dict[34] = time_dict.get(34,0) + time.time() - prev_time
prev_time = time.time()
for i in range(4000):
    time_dict[36] = time_dict.get(36,0) + time.time() - prev_time
    prev_time = time.time()
    input = torch.randn(1, 1, 32, 32)
    time_dict[37] = time_dict.get(37,0) + time.time() - prev_time
    prev_time = time.time()
    out = net(input)
    time_dict[38] = time_dict.get(38,0) + time.time() - prev_time
    prev_time = time.time()
    saved.append(out)
    time_dict[39] = time_dict.get(39,0) + time.time() - prev_time
    prev_time = time.time()
time_dict[40] = time_dict.get(40,0) + time.time() - prev_time
prev_time = time.time()

json.dump(time_dict, f_time)