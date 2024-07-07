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



## Run Model

```
git clone https://github.com/ben-z-original/omnicrack30k
conda create --name py310 python=3.10
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
Run model on single image. If a path to a folder is provided, it runs on the files in the folder.
```
python -m omnicrack30k.inference assets/UAV75_DSC00573.png
```
### Evaluation
To compute the centerline IoU (clIoU) with tolerance 4px, e.g., on the ```test set``` for the ```Ceramic``` subset, run:
```
python -m omnicrack30k.evaluation path_to_omnicrack30k_rootdir test --subset Ceramic
```

## Dataset(s)

### Overview
![image](https://github.com/ben-z-original/omnicrack30k/assets/85626335/618579da-8f02-41c8-8a09-657bc18de859)


![image](https://github.com/ben-z-original/omnicrack30k/assets/85626335/7a09d4d1-8dc0-40b1-8a1c-74a6c0e7b9d9)

### Download
Due to license issues, the dataset cannot openly be shared. If you need access for research purposes to replicate our results, etc., kindly send a request mail from your university/education account to christian.benz@uni-weimar.de with the following content, which you thereby acknowledge:

```Subject: Access OmniCrack30k Dataset```

```
Kindly grant me access to the OmniCrack30k dataset.

I hereby confirm, that I comply with all licenses involved, especially the ones related to the data subsets.
I will use the dataset for non-commercial purposes only.

Kind regards,
[Full name, job role, institution, link to personal university/research website]
```

## References
Don't forget to give credit to the partly excellent work done by the following authors in terms of creation and provision of crack segmentation datasets:

####  AEL
```
@article{amhaz2015automatic,
	title={Automatic crack detection on 2d pavement images: An algorithm based on minimal path selection, accepted to ieee trans},
	author={Amhaz, R and Chambon, S and Idier, J and Baltazart, V},
	journal={Intell. Transp. Syst},
	year={2015}
}
```
#### BCL
[Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TUFAJT)
```
@article{ye2021structural,
	title={Structural crack detection from benchmark data sets using pruned fully convolutional networks},
	author={Ye, Xiao-Wei and Jin, T and Li, ZX and Ma, SY and Ding, Y and Ou, YH},
	journal={Journal of Structural Engineering},
	volume={147},
	number={11},
	pages={04721008},
	year={2021},
	publisher={American Society of Civil Engineers}
}
```
#### Ceramic
[Github](https://github.com/gerivansantos/ceramic-cracks-dataset.git)
```
@article{junior2021ceramic,
	title={Ceramic cracks segmentation with deep learning},
	author={Junior, Gerivan Santos and Ferreira, Janderson and Mill{\'a}n-Arias, Cristian and Daniel, Ramiro and Junior, Alberto Casado and Fernandes, Bruno JT},
	journal={Applied Sciences},
	volume={11},
	number={13},
	pages={6017},
	year={2021},
	publisher={MDPI}
}
```
#### CFD
[Github](https://github.com/cuilimeng/CrackForest-dataset)
```
@article{shi2016automatic,
	title={Automatic road crack detection using random structured forests},
	author={Shi, Yong and Cui, Limeng and Qi, Zhiquan and Meng, Fan and Chen, Zhensong},
	journal={IEEE Transactions on Intelligent Transportation Systems},
	volume={17},
	number={12},
	pages={3434--3445},
	year={2016},
	publisher={IEEE}
}
```
#### CRACK500
[Github](https://github.com/fyangneil/pavement-crack-detection)
```
@inproceedings{zhang2016road, 
	title={Road crack detection using deep convolutional neural network}, 
	author={Zhang, Lei and Yang, Fan and Zhang, Yimin Daniel and Zhu, Ying Julie}, 
	booktitle={Image Processing (ICIP), 2016 IEEE International Conference on}, 
	pages={3708--3712}, 
	year={2016}, 
	organization={IEEE} 
}
@article{yang2019feature,
	title={Feature pyramid and hierarchical boosting network for pavement crack detection},
	author={Yang, Fan and Zhang, Lei and Yu, Sijia and Prokhorov, Danil and Mei, Xue and Ling, Haibin},
	journal={IEEE Transactions on Intelligent Transportation Systems},
	volume={21},
	number={4},
	pages={1525--1535},
	year={2019},
	publisher={IEEE}
}
```
#### CrackLS315, CrackTree260, CRKWH100, and Stone331
[Github](https://github.com/qinnzou/DeepCrack)
```
@article{zou2018deepcrack,
	title={Deepcrack: Learning hierarchical convolutional features for crack detection},
	author={Zou, Qin and Zhang, Zheng and Li, Qingquan and Qi, Xianbiao and Wang, Qian and Wang, Song},
	journal={IEEE Transactions on Image Processing},
	volume={28},
	number={3},
	pages={1498--1512},
	year={2018},
	publisher={IEEE}
}
@article{zou2012cracktree,
	title={CrackTree: Automatic crack detection from pavement images},
	author={Zou, Qin and Cao, Yu and Li, Qingquan and Mao, Qingzhou and Wang, Song},
	journal={Pattern Recognition Letters},
	volume={33},
	number={3},
	pages={227--238},
	year={2012},
	publisher={Elsevier}
}
```
#### CrSpEE
[Github](https://github.com/OSUPCVLab/CrSpEE)
```
@article{bai2021detecting,
	title={Detecting cracks and spalling automatically in extreme events by end-to-end deep learning frameworks},
	author={Bai, Yongsheng and Sezen, Halil and Yilmaz, Alper},
	journal={ISPRS Annals of the Photogrammetry, Remote Sensing and Spatial Information Sciences},
	volume={2},
	pages={161--168},
	year={2021},
	publisher={Copernicus GmbH}
}
```
#### CSSC
[Github](https://github.com/CCNYRoboticsLab/concreteIn_inpection_VGGF)

Full resolution data (shared with the consent of the authors; mind the original repository available via the link above):<br>
[Crack Data (full res)](https://www.dropbox.com/s/sak67svf9fbvepi/partialCrackDataSet.rar?dl=0)<br>
[Spalling Data (full res)](https://www.dropbox.com/s/wenjq3hguli41bg/spallingDataset.rar?dl=0)

Import note from the authors: <br>
Please remember that this data set is research only (${{\color{red}\textsf{US law required, you take your own risk on this}}}\$), not for commercial use. 

```
@inproceedings{yang2017deep,
	title={Deep concrete inspection using unmanned aerial vehicle towards cssc database},
	author={Yang, Liang and Li, Bing and Li, Wei and Liu, Zhaoming and Yang, Guoyong and Xiao, Jizhong},
	booktitle={Proceedings of the IEEE/RSJ international conference on intelligent robots and systems},
	pages={24--28},
	year={2017}
}
```
#### DeepCrack
[Github](https://github.com/yhlleo/DeepCrack)
```
@article{liu2019deepcrack,
	title={DeepCrack: A deep hierarchical feature learning architecture for crack segmentation},
	author={Liu, Yahui and Yao, Jian and Lu, Xiaohu and Xie, Renping and Li, Li},
	journal={Neurocomputing},
	volume={338},
	pages={139--153},
	year={2019},
	publisher={Elsevier}
}

```
#### DIC
[Zenodo](https://zenodo.org/record/4307686)
```
@article{rezaie2020comparison,
	title={Comparison of crack segmentation using digital image correlation measurements and deep learning},
	author={Rezaie, Amir and Achanta, Radhakrishna and Godio, Michele and Beyer, Katrin},
	journal={Construction and Building Materials},
	volume={261},
	pages={120474},
	year={2020},
	publisher={Elsevier}
}
```
#### GAPS384
[TU Ilmenau](https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-informatik-und-automatisierung/profil/institute-und-fachgebiete/institut-fuer-technische-informatik-und-ingenieurinformatik/fachgebiet-neuroinformatik-und-kognitive-robotik/data-sets-code/german-asphalt-pavement-distress-dataset-gaps)
[Github](https://github.com/fyangneil/pavement-crack-detection)
```
@inproceedings{eisenbach2017get,
	title={How to get pavement distress detection ready for deep learning? A systematic approach},
	author={Eisenbach, Markus and Stricker, Ronny and Seichter, Daniel and Amende, Karl and Debes, Klaus and Sesselmann, Maximilian and Ebersbach, Dirk and Stoeckert, Ulrike and Gross, Horst-Michael},
	booktitle={2017 international joint conference on neural networks (IJCNN)},
	pages={2039--2047},
	year={2017},
	organization={IEEE}
}
@inproceedings{stricker2019improving,
	title={Improving visual road condition assessment by extensive experiments on the extended gaps dataset},
	author={Stricker, Ronny and Eisenbach, Markus and Sesselmann, Maximilian and Debes, Klaus and Gross, Horst-Michael},
	booktitle={2019 International Joint Conference on Neural Networks (IJCNN)},
	pages={1--8},
	year={2019},
	organization={IEEE}
}
@article{yang2019feature,
	title={Feature pyramid and hierarchical boosting network for pavement crack detection},
	author={Yang, Fan and Zhang, Lei and Yu, Sijia and Prokhorov, Danil and Mei, Xue and Ling, Haibin},
	journal={IEEE Transactions on Intelligent Transportation Systems},
	volume={21},
	number={4},
	pages={1525--1535},
	year={2019},
	publisher={IEEE}
}
```
#### Khanh11k
[Github](https://github.com/khanhha/crack_segmentation)

#### LCW
[Virginia Tech](https://data.lib.vt.edu/articles/dataset/Labeled_Cracks_in_the_Wild_LCW_Dataset/16624672)
```
@article{bianchi2022development,
	title={Development of Extendable Open-Source Structural Inspection Datasets},
	author={Bianchi, Eric and Hebdon, Matthew},
	journal={Journal of Computing in Civil Engineering},
	volume={36},
	number={6},
	pages={04022039},
	year={2022},
	publisher={American Society of Civil Engineers}
}
```
#### Masonry
[Github](https://github.com/dimitrisdais/crack_detection_CNN_masonry)
```
@article{dais2021automatic,
	title={Automatic crack classification and segmentation on masonry surfaces using convolutional neural networks and transfer learning},
	author={Dais, Dimitris and Bal, Ihsan Engin and Smyrou, Eleni and Sarhosis, Vasilis},
	journal={Automation in Construction},
	volume={125},
	pages={103606},
	year={2021},
	publisher={Elsevier}
}
```
#### S2DS
[Github](https://github.com/ben-z-original/s2ds)
```
@inproceedings{benz2022image,
	title={Image-Based Detection of Structural Defects Using Hierarchical Multi-scale Attention},
	author={Benz, Christian and Rodehorst, Volker},
	booktitle={DAGM German Conference on Pattern Recognition},
	pages={337--353},
	year={2022},
	organization={Springer}
}
```
#### TopoDS
[Github](https://zenodo.org/record/6651663) 
```
@article{pantoja2022topo,
	title={TOPO-Loss for continuity-preserving crack detection using deep learning},
	author={Pantoja-Rosero, Bryan G and Oner, D and Kozinski, Mateusz and Achanta, Radhakrishna and Fua, Pascal and P{\'e}rez-Cruz, Fernando and Beyer, K},
	journal={Construction and Building Materials},
	volume={344},
	pages={128264},
	year={2022},
	publisher={Elsevier}
}
```
#### UAV75
[Github](https://github.com/ben-z-original/uav75)
```
@inproceedings{benz2019crack,
	title={Crack segmentation on UAS-based imagery using transfer learning},
	author={Benz, Christian and Debus, Paul and Ha, Huy Khanh and Rodehorst, Volker},
	booktitle={2019 International Conference on Image and Vision Computing New Zealand (IVCNZ)},
	pages={1--6},
	year={2019},
	organization={IEEE}
}
```
