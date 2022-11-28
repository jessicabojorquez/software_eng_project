import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5, padding="same")
        self.conv2 = nn.Conv2d(6, 10, 3, padding="same")
        self.pool = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(10, 16, 3, padding="same")
        self.conv4 = nn.Conv2d(16, 16, 3, padding="same")
        self.pool = nn.MaxPool2d(2, 2)
        self.conv5 = nn.Conv2d(16, 10, 3, padding="same")
        self.conv6 = nn.Conv2d(10, 10, 3)
        self.fc1 = nn.Linear(360, 128)
        self.fc2 = nn.Linear(128, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.relu(self.conv2(F.relu(self.conv1(x))))
        x = self.pool(x)
        x = F.relu(self.conv4(F.relu(self.conv3(x))))
        x = self.pool(x)
        x = F.relu(self.conv6(F.relu(self.conv5(x))))
        x = x.view(-1, 360)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x