# Median Filter

## An example of when it is useful to use the median filter.

![Original Image](Questionario-3-imagem-3.png)

There is salt and pepper impulsive noise in the original image. Using the median filter, it is possible to reduce that noise, since too high or too low values tend to be filtered out.

| ![Kernel Size 3 Result](results/kernel_3.png) |
| :-------------------------------------------: |
|               *Kernel Size = 3*               |

| ![Kernel Size 5 Result](results/kernel_5.png) |
| :-------------------------------------------: |
|               *Kernel Size = 5*               |

| ![Kernel Size 7 Result](results/kernel_7.png) |
| :-------------------------------------------: |
|               *Kernel Size = 7*               |

Notice that larger kernerls result in less noise, but also in a more washed-out look.