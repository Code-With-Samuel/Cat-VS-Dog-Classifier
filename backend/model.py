# Your ResNet18 model


import torch
from torch import nn
import lightning as L
import torch.nn.functional as F

class CatDogModel(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)  # input: 3 channels (RGB), output: 16 filters
        self.pool = nn.MaxPool2d(2, 2)               # reduces size
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.fc1 = nn.Linear(32 * 8 * 8, 64)          # depends on input image size (e.g. 32x32)
        self.fc2 = nn.Linear(64, 2)                   # 2 classes: cat or dog

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))  # Conv1 → ReLU → MaxPool
        x = self.pool(F.relu(self.conv2(x)))  # Conv2 → ReLU → MaxPool
        x = x.view(x.size(0), -1)             # flatten
        x = F.relu(self.fc1(x))               # Fully connected
        return self.fc2(x)                    # Final layer (logits)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        acc = (logits.argmax(dim=1) == y).float().mean()
        self.log("train_loss", loss)
        self.log("train_acc", acc)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.001)
