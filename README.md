# Julia Sets

A Julia set can be defined to be the set of initial conditions ![formula](https://render.githubusercontent.com/render/math?math=z_0) which produce a bounded sequence {![formula](https://render.githubusercontent.com/render/math?math={z_n})} when the recurrence relation

![formula](https://render.githubusercontent.com/render/math?math=z_{n%2B1}) = ![formula](https://render.githubusercontent.com/render/math?math=f(z)) = ![formula](https://render.githubusercontent.com/render/math?math=z^{2}_{n}) + ![formula](https://render.githubusercontent.com/render/math?math=c)

is iterated, for a given complex constant ![formula](https://render.githubusercontent.com/render/math?math=c). 

<img width="806" alt="image" src="https://user-images.githubusercontent.com/40894018/166339016-be3b4d2c-da79-4890-88bd-dcb207881966.png">

This project begins by computing and plotting Julia sets such that ![formula](https://render.githubusercontent.com/render/math?math=c) = ![formula](https://render.githubusercontent.com/render/math?math=-1), with ![formula](https://render.githubusercontent.com/render/math?math=Re(z)) ∈ [−2, 2] and ![formula](https://render.githubusercontent.com/render/math?math=Im(z)) ∈ [−1, 1].
Then we investigate the cycle of different Julia sets, different powers of ![formula](https://render.githubusercontent.com/render/math?math=z) and  the maximum number of iterations. We also discuss Julia and Fatou set plots. Julia and Fatou set plots are often colour coded according to how many iterations are required to reach infinity (or whatever large number is approximating infinity). In such a scheme the filled Julia set is black (points never reach infinity). Finally we plot the Mandelbrot - this is the set of all values of ![formula](https://render.githubusercontent.com/render/math?math=c) for which the corresponding Julia sets are connected. 
