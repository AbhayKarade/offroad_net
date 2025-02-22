"""
ref:
1. https://kozodoi.me/python/deep%20learning/pytorch/tutorial/2021/03/08/image-mean-std.html
2. https://www.binarystudy.com/2021/04/how-to-calculate-mean-standard-deviation-images-pytorch.html
"""
import os

import torchvision
from torchvision import transforms

import torch
from torch.utils.data import DataLoader


def batch_mean_and_sd(loader):
    cnt = 0
    fst_moment = torch.empty(3)
    snd_moment = torch.empty(3)

    for images, _ in loader:
        b, c, h, w = images.shape
        nb_pixels = b * h * w
        sum_ = torch.sum(images, dim=[0, 2, 3])
        sum_of_square = torch.sum(images ** 2,
                                  dim=[0, 2, 3])
        fst_moment = (cnt * fst_moment + sum_) / (cnt + nb_pixels)
        snd_moment = (cnt * snd_moment + sum_of_square) / (cnt + nb_pixels)
        cnt += nb_pixels

    mean, std = fst_moment, torch.sqrt(snd_moment - fst_moment ** 2)
    return mean, std


def get_image_data(data_root, img_dir="images"):
    # data_path = os.path.join(data_root, img_dir)
    data_path = data_root

    transform_img = transforms.Compose([
        # transforms.Resize(256),
        # transforms.CenterCrop(256),
        transforms.ToTensor(),
    ])

    image_data = torchvision.datasets.ImageFolder(
        root=data_path, transform=transform_img
    )

    return image_data


def calc_mean_std_dev(data_root, img_dir="images"):
    # image_data = get_image_data(data_root, img_dir)
    image_data = get_image_data(data_root)

    image_data_loader = DataLoader(
        image_data,
        batch_size=len(image_data),
        shuffle=False,
        num_workers=0
    )

    return image_data_loader


def batch_mean_std(data_root, img_dir="images", batch_size=2):
    # image_data = get_image_data(data_root, img_dir)
    image_data = get_image_data(data_root)

    loader = DataLoader(
        image_data,
        batch_size=batch_size,
        num_workers=1)

    mean, std = batch_mean_and_sd(loader)
    return mean, std


def mean_std(loader):
    images, labels = next(iter(loader))
    # shape of images = [b,c,w,h]
    mean, std = images.mean([0, 2, 3]), images.std([0, 2, 3])
    return mean, std


def main():
    list_datasets = [
        "ms_yamaha",
        "ms_rugd",
    ]
    for data_root in list_datasets:
        image_data_loader = calc_mean_std_dev(data_root, img_dir="images")

        mean, std = mean_std(image_data_loader)
        print(f"Dataset: {data_root}"
              f"\nmean: \n{mean}"
              f"\nstd_dev: \n{std}")

        scaled_mean = 255 * mean
        scaled_std_dev = 255 * std
        print(f"Dataset: {data_root}"
              f"\nscaled_mean: \n{scaled_mean}"
              f"\nscaled_std_dev: \n{scaled_std_dev}")


"""
Starting to run: python src/calc_image_stats.py 
Dataset: ms_yamaha
mean: 
tensor([0.4294, 0.4478, 0.4247])
std_dev: 
tensor([0.2664, 0.2653, 0.2674])
Dataset: ms_yamaha
scaled_mean: 
tensor([109.4993, 114.1997, 108.3029])
scaled_std_dev: 
tensor([67.9276, 67.6512, 68.1809])

Dataset: ms_rugd
mean: 
tensor([0.4038, 0.4037, 0.4016])
std_dev: 
tensor([0.2739, 0.2757, 0.2782])
Dataset: ms_rugd
scaled_mean: 
tensor([102.9630, 102.9438, 102.3976])
scaled_std_dev: 
tensor([69.8548, 70.3098, 70.9376])
"""

if __name__ == '__main__':
    main()
