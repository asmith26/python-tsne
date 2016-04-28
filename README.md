# python-tsne
Copied from [original implement](http://lvdmaaten.github.io/tsne/) + my tweaks
(add PyLab problems)

Add image-based tSNE (i.e. images that are nearby each other are also close in the CNN representation space - similarities are more often class-based and semantic rather than pixel and color-based) following [CS231n](http://cs231n.github.io/understanding-cnn/):
> To produce an embedding, we can take a set of images and use the ConvNet to extract the CNN codes (e.g. in AlexNet the 4096-dimensional vector right before the classifier, and crucially, including the ReLU non-linearity). We can then plug these into t-SNE and get 2-dimensional vector for each image.
