import torch
import torch.nn as nn


class Encoder(nn.Module):
    def __init__(self, hidden_dim: int) -> None:
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Linear(1245, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, hidden_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.encoder(x)
        return x


class Decoder(nn.Module):
    def __init__(self, hidden_dim: int) -> None:
        super().__init__()

        self.decoder = nn.Sequential(
            nn.Linear(hidden_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 1245),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.decoder(x)
        return x


class AutoEncoder(nn.Module):
    def __init__(
        self, 
        hidden_dim: int = 128,
    ) -> None:
        super().__init__()

        self.encoder = Encoder(hidden_dim)

        self.decoder = Decoder(hidden_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.encoder(x)
        x = self.decoder(x)
        return x
