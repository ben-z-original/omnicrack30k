![gradio_demo](https://github.com/ben-z-original/omnicrack30k/assets/85626335/d4216a56-58dc-4b57-ba91-30ce5b62e17f)

# OmniCrack30k
*OmniCrack30k* is a compilation of datasets for structural crack segmentation. The best performing model is provided in this repo, kindly also checkout the corresponding huggingface demo:

![image](https://github.com/ben-z-original/omnicrack30k/assets/85626335/b99341fa-0a14-4afe-be52-f0489fa506e1)
[Huggingface Demo](https://huggingface.co/spaces/chrisbe/omnicrack30k-crack-segmentation)
![image](https://github.com/ben-z-original/omnicrack30k/assets/85626335/8269551b-c0fc-4c92-bb3b-26481568b788)


It only runs on CPU, so for large images it takes longer. The images above from the BCL dataset are 256×256 and took about 2 seconds.


## Citation
[CVPRW Paper](https://openaccess.thecvf.com/content/CVPR2024W/VAND/papers/Benz_OmniCrack30k_A_Benchmark_for_Crack_Segmentation_and_the_Reasonable_Effectiveness_CVPRW_2024_paper.pdf)

If you find our work useful, kindly cite accordingly:
```
@InProceedings{Benz_2024_CVPR,
    author    = {Benz, Christian and Rodehorst, Volker},
    title     = {OmniCrack30k: A Benchmark for Crack Segmentation and the Reasonable Effectiveness of Transfer Learning},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
    month     = {June},
    year      = {2024}
}
```



## Overview
![image](https://github.com/ben-z-original/omnicrack30k/assets/85626335/618579da-8f02-41c8-8a09-657bc18de859)


![image](https://github.com/ben-z-original/omnicrack30k/assets/85626335/7a09d4d1-8dc0-40b1-8a1c-74a6c0e7b9d9)

## Run Model

```
git clone https://github.com/ben-z-original/omnicrack30k
conda create -name py310 python=3.10
conda activate py310
cd omnicrack30k
pip install -e .
```
The plan, i.e. the trained parameters, will be automatically downloaded when one of the commands below is run, but can also be accessed via:
[Google Drive Link](https://drive.google.com/file/d/15S1dvjr7050kISlQ0JTiEPA1eeUDfoOl/view?usp=drive_link)

### Start Local Gradio App
The following command starts a local gradio app, which can be opened in the web browser, e.g., at http://127.0.0.1:7860. The infos and warnings concerning nnU-Net can be ignored.
```
python -m omnicrack30k.inference
```
### Single Image
If you provide a path to a folder it also runs on the files in the folder.
```
python -m omnicrack30k.inference assets/UAV75_DSC00573.png
```



## Download Dataset(s)


<p align="center">
<b>Recipes for downloading and preparing the dataset as well as the nnU-Net benchmarking model will be published on <br><br>
July 5, 2024</b>
</p>
