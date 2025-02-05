from __future__ import absolute_import, division, print_function

import torch
import numpy as np

color_correlation_svd_sqrt = np.asarray(
    [[0.26, 0.09, 0.02], [0.27, 0.00, -0.05], [0.27, -0.09, 0.03]]
).astype("float32")

max_norm_svd_sqrt = np.max(np.linalg.norm(color_correlation_svd_sqrt, axis=0))

color_correlation_normalized = color_correlation_svd_sqrt / max_norm_svd_sqrt

color_mean = [0.48, 0.46, 0.41]


def _linear_decorrelate_color(tensor):
    t_permute = tensor.permute(0, 2, 3, 1)
    t_permute = torch.matmul(
        t_permute, torch.tensor(color_correlation_normalized.T).to(t_permute.device)
    )
    tensor = t_permute.permute(0, 3, 1, 2)
    return tensor


def to_valid_rgb(image_f, decorrelate=False):
    def inner():
        image = image_f()
        if decorrelate:
            image = _linear_decorrelate_color(image)
        return torch.sigmoid(image)

    return inner
