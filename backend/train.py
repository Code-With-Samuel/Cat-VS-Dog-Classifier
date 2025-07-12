# Training script


from model import CatDogModel
from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.utils.data import DataLoader
import lightning as L

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
])

train_data = CIFAR10(root='data/', train=True, transform=transform, download=True)
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

model = CatDogModel()

trainer = L.Trainer(max_epochs=5)
trainer.fit(model, train_loader)
