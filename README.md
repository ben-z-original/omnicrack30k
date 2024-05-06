# OmniCrack30k
## Overview

![image](https://github.com/ben-z-original/omnicrack30k/assets/85626335/7a09d4d1-8dc0-40b1-8a1c-74a6c0e7b9d9)

## Download

Due to license issues the dataset can unfortunately not be redistributed as one. Thus, they need to be downloaded from the original sources and prepared according to the following recipes.

### S2DS, UAV75, Khanh11k
These datasets are directly provided due to the authors' (partial) involvement of the acquisition and creation process.

### AEL
\footnote{\url{https://www.irit.fr/~Sylvie.Chambon/Crack_Detection_Database.html}, accessed August 16, 2023.}: The dataset AEL -- an acronym of the subsets -- was published by \textcite{amhaz2015automatic}. It consists of the three subsets, AIGLE\textunderscore RN, ESAR, and LCMS. Last of which provides images of low quality. The images are of variable sizes and exclusively show \textit{asphalt} cracks.

### BCL
\footnote{\url{https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/RURXSH}, accessed August 16, 2023.}: Details of the \textit{Bridge Crack Library} (BCL) are provided in \textcite{ye2021structural}. The samples are patches from larger images. The cracks are shown in a macro-like fashion which can account for the visible blur in many samples. 2,036 samples show cracks in \textit{steel}, 5,769 cracks in \textit{concrete} and \textit{stone}, and 3,195 are negatives samples for crack-line artifacts. No information on data splits are provided. Featuring only synthetic cracks BCL\,2.0 is disregarded here\footnote{\url{https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TUFAJT}, accessed August 17.2023.}.

### Ceramic
\footnote{\url{https://github.com/gerivansantos/ceramic-cracks-dataset}, accessed August 16, 2023.}: Published in the context of \textcite{junior2021ceramic}. No labels are provided for the test set. The images show cracks in a large variety of \textit{ceramic} tiles.
	
### CFD
\footnote{\url{https://github.com/cuilimeng/CrackForest-dataset}, accessed August 16, 2023.}: Short for \textit{CrackForest} dataset. Published as part of \textcite{shi2016automatic}. The images show pavement cracks almost exclusively in \textit{asphalt} surfaces. The exact split into training and test set is unknown; the share is 60\%/40\%. 
	
### Conglomerate
\footnote{\url{https://data.lib.vt.edu/articles/dataset/Concrete_Crack_Conglomerate_Dataset/16625056}, accessed August 16, 2023.}: Used in publication \textcite{bianchi2022development}. Based on Khanh11k it forms a collection of datasets including CFD, Crack500, CrackTree200, DeepCrack, GAPs, etc. 
	
### CRACK500
\footnote{\url{https://github.com/fyangneil/pavement-crack-detection}, accessed August 16, 2023.}: The dataset is provided in the context of \textcite{yang2019feature}. The origin of the dataset can be traced to \textcite{zhang2016road} who, however, seem to not provide any download link. The provided images by \textcite{yang2019feature} happen to be smaller than the size reported by \parencite{zhang2016road}. The images are varying in size and exclusively show \textit{pavement} cracks of variable widths.
	
### CrackLS315
\footnote{\url{https://github.com/qinnzou/DeepCrack}, accessed August 16, 2023.}: Published in connection with \textcite{zou2018deepcrack}. The images show \textit{asphalt} cracks with slight illumination inhomogeneities.
	
### CrackSeg9k
\footnote{\url{https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/EGIEBY}, accessed August 16, 2023.}: \textcite{kulkarni2022crackseg9k} combined and transformed the Khanh11k, Masonry, and Ceramic datasets. As of August 16, 2023 the downloadable dataset encompassed roughly 6k samples instead of the supposed 9k.%, primarily due to the missing CRACK500 subset. 
	
### CrackTree200
\footnote{Download as part of CrackTree260, \url{https://github.com/qinnzou/DeepCrack}, accessed August 16, 2023.}: Also referred to as CrackTree206 was published by \textcite{zou2012cracktree}. It exclusively shows \textit{asphalt} crack in relatively homogeneous conditions.	
 
### CrackTree260
\footnote{\url{https://github.com/qinnzou/DeepCrack}, accessed August 16, 2023.}: Is an extension of CrackTree200 and was published by \textcite{zou2018deepcrack}. CrackTree200 was extended by images with lower quality and cracks with sophisticated net-like structure. All images show \textit{asphalt} cracks under relatively homogeneous conditions. 

### CRKWH100
\footnote{\url{https://github.com/qinnzou/DeepCrack}, accessed August 16, 2023.}: Published in connection with \textcite{zou2018deepcrack}. The images show \textit{asphalt} cracks with slight illumination inhomogeneities. It contains five images with white cracks\footnote{The segmentation of white cracks is not a subject of this theses. For dataset consistency the images with white cracks are, however, kept in the CRKWH100 dataset.}.

### CrSpEE
\footnote{\url{https://github.com/OSUPCVLab/CrSpEE}, accessed August 16, 2023.}: The \textit{Crack and Spalling Dataset in Context of Extreme Events} (CrSpEE) is a dataset for instance segmentation of cracks and spalling published by \textcite{bai2021detecting}. It shows cracks (and spalling) `in the wild', i.e.\ on challenging images with a substantial amount of distractors (people, context, background, etc.). Due to partly large image sizes and the reduced added value of the negative samples provided, the training set was filtered for cracks.

### CSSC
\footnote{\url{https://github.com/CCNYRoboticsLab/concreteIn_inpection_VGGF}, accessed August 16, 2023.}: The \textit{Concrete Structure Spalling and Crack} dataset (CSSC) was published by \textcite{yang2017deep}. All samples were systematically augmented by a horizontal and vertical flip. Since data augmentation usually delegated to the training procedure, the augmented versions are removed. The images show cracks mostly in \textit{concrete} and \textit{stone} as well as spalling. Adding no substantial value, the spalling subset was removed from the training set.

### DeepCrack
\footnote{\url{https://github.com/yhlleo/DeepCrack}, accessed August 17, 2023.}: The dataset was published together with the DeepCrackL approach \parencite{liu2019deepcrack}. The images show cracks of variable widths (including very wide cracks) in different surfaces such as concrete and stone. Some images are blurry.

### DIC
\footnote{\url{https://zenodo.org/record/4307686}, accessed August 17, 2023.}: Published in the context of \textcite{rezaie2020comparison} which investigates digital image correlation (DIC) for deformable image matching. The images show crack on a \textit{plastered} wallett (a specimen) with random black speckles under homogeneous, lab-like conditions.

### GAPS384
\footnote{\url{https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-informatik-und-automatisierung/profil/institute-und-fachgebiete/institut-fuer-technische-informatik-und-ingenieurinformatik/fachgebiet-neuroinformatik-und-kognitive-robotik/data-sets-code/german-asphalt-pavement-distress-dataset-gaps}, accessed November 10, 2023.}: \textcite{eisenbach2017get}, \textcite{stricker2019improving}, and \textcite{stricker2021road} published a series of three datasets under the name GAPs (\textit{German Asphalt Pavement Distress}) v1, v2, and 10m. GAPs\,v1 and GAPs\,v2 provide patch classification labels only. GAPs\,10m contains very coarse segmentation annotations\footnote{Given the very coarse labels, the low number of cracks, and the already widely covered domain of asphalt cracks, GAPs\,10m is assumed to not add substantial value to the considered datasets. Image sizes of 11505$\times $5030\,px and reduced accessibility, furthermore, impede the handling of the dataset. GAPs\,10m is, thus, disregarded in this work.}. \textcite{yang2019feature} appear to have create pixel-wise labels for GAPs v1 which they released as GAPS384\footnote{As segmentation label creators \textcite{yang2019feature} are listed as primary authors of GAPS384. The credit to the images, however, go to \parencite{eisenbach2017get}, \url{https://www.tu-ilmenau.de/universitaet/fakultaeten/fakultaet-informatik-und-automatisierung/profil/institute-und-fachgebiete/institut-fuer-technische-informatik-und-ingenieurinformatik/fachgebiet-neuroinformatik-und-kognitive-robotik/data-sets-code/german-asphalt-pavement-distress-dataset-gaps}.}. The images show \textit{asphalt} cracks under relatively homogeneous conditions.

### LCW
\footnote{\url{https://data.lib.vt.edu/articles/dataset/Labeled_Cracks_in_the_Wild_LCW_Dataset/16624672}, accessed August 16, 2023.}: The \textit{Labeled Cracks in the Wild} (LCW) dataset was published in the context of \textcite{bianchi2022development} and features crack detection under challenging conditions. The images are mostly of lower quality and show the structure's context including steel beams, other support elements, spreading vegetation, landscape backgrounds, etc. Due to the high number of negative samples, the training set is reduced to images containing cracks. The images almost exclusively show cracks in \textit{concrete}.

### Masonry
\footnote{\url{https://github.com/dimitrisdais/crack_detection_CNN_masonry}, accessed August 16, 2023.}: Published in the context of \textcite{dais2021automatic}. The images show crack in variable kinds of \textit{masonry} most of which are brick walls. The negative samples are not provided. Due to lack of information the re-establishment of the train/test split is probably flawed.

### Kaggle11k
\footnote{\url{https://www.kaggle.com/datasets/lakshaymiddha/crack-segmentation-dataset}, accessed August 16, 2023.}: As the subsequent overlap analysis will show, an identical copy of Khanh11k without reference.

### Khanh11k
\footnote{\url{https://github.com/khanhha/crack_segmentation}, accessed August 16, 2023.}: There exists no naming convention for this dataset. The name \textit{Khanh11k} is proposed: it refers to the name of the repository owner and the approximate number of samples. Khanh11k is a collection of other datasets including CrackTree200, CFD, CRACK500, DeepCrack, and parts of AEL. Labels were stored in JPG format which potentially accounts for artifacts in some labels. Many images were patched and unisotropicly scaled which led to distortions.

### S2DS
\footnote{\url{https://github.com/ben-z-original/s2ds}, accessed August 17, 2023.}: The \textit{Structural Defects Dataset} (S2DS) was created in the context of this thesis and published in connection with \textcite{benz2022image}. It contains cracks alongside other classes in the representation required for real-world bridge inspection e.g., by means of UAS. Due to the limited number of images, also the negative samples are kept. Further details are provided in Section\,\ref{sec:s2ds}.

### Stone331
\footnote{\url{https://github.com/qinnzou/DeepCrack}}: Published in connection with \textcite{zou2018deepcrack}. The images show cracks in \textit{stone} under homogeneous conditions. 

### TopoDS
\footnote{\url{https://zenodo.org/record/6651663}, accessed August 17, 2023.}: Published in the context of \textcite{pantoja2022topo}. TopoDS forms an `in the wild' dataset with challenging images containing a multitude of distractors (other structural support structures, background objects, etc.). The centerline annotations often are coarse and show offsets to the presumed centerline. The images show cracks on a multitude of structures in a post-disaster scenario. Demolition edges of spallings are also labeled as crack.

### UAV75
\footnote{\url{https://github.com/christiab/uav75}, accessed August 17, 2023.}: The \textit{Unmanned Aerial Vehicle} dataset (UAV75) was created in the context of this thesis and published in connection with \textcite{benz2019crack}. It represents cracks in a real-world inspection scenario with images captured by a UAS where cracks regularly occur as 1-5\,px wide structures. The artifacts resulting from weathering and shadow cast on the planking structures form a distractor featured in the `planking pattern' class.
