# Brain-Download-Datasets

## Datasets
The dataset contain EEG signals recorded from `EMOTIV Insight` 5-channel headset of four different experiments. All the following experiments except for *Baseline* were conducted by visually stimulating the subject's brain with a random image presentation. The image sequencing was done using the [Brain Download](https://github.com/LKbrilliant/Brain-Download) software. 

1. **Baseline**: EEG signals of calmed mind with eyes opened and closed.
2. **Image-Blank**: Simulated thinking “something” and “nothing” on the subject’s brain by randomly presenting images and blank screens.

<p align="center">
  <img src="Media/Image-Blank.gif" alt="Image-Blank" width="800"/>
</p>

3. **Left-Right_Arrows**: Showed left and right directed arrows on the left and right edges of the screen respectively and the subject was instructed to directly look at them without moving the head. Since the image sequence is randomized, a reference mark was presented at the center of the screen after each arrow image.

<p align="center">
<img src="Media/Left-Right.gif" alt="Left-Right_Arrows" width="800"/>
</p>

4. **Visual_Q&A**: Simultaneously displayed a YES or NO answerable question about the presented image and instructed the subject to think about the answer.

<p align="center">
<img src="Media/Yes-No.gif" alt="Visual_Q&A" width="800"/>
</p>

## Scripts
- After extracting the `.zip` files in the Dataset directory, you can plot a random record (.csv file) using `plot_random_full.py`.
- You can split the records (.csv files) into smaller chunks of watching one stimulus by using the `splitter.py` script. The separated chunks and their labels will be saved as `.npy` files. 
- You can plot some random chunks in a saved `.npy` data file by using the `plot_random_split.py`.

## Experiment Details
All the data samples from the above mentioned experiments were collected using one male subject (25 years old). The following table shows the details of the performed experiments. 

| Property | Image-Blank | Left-Right | Visual_Q&A |
| -------- | ----------- | ----------------- | ---------- |
| Number of classes |`2` (Image, Blank)| `3` (Center, Left, Right)| `2` (Yes, No) | 
| Number of images in the image-set | `500` | `320` | `250` |
| Image resolution | `1200x800 pixels` | `1896x790 pixels` | `1200x800 pixels` | 
| Screen time for an image | `2 seconds` | `2 seconds` |`2 seconds` |
| Image presentations per record(.csv file) | `20` | `20` | `20` | 
| Number of records | `500` | `300` | `250` |
| Total stimuli observed | `10,000` | `6,000` | `5,000` |