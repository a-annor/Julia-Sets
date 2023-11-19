# Julia Sets

A Julia set can be defined to be the set of initial conditions $z_0$ which produce a bounded sequence $z_n$ when the recurrence relation

$$z_{n+1} = f(z) = z^{2}_{n} + c$$

is iterated, for a given complex constant $c$. 

<img width="806" alt="image" src="https://user-images.githubusercontent.com/40894018/166339016-be3b4d2c-da79-4890-88bd-dcb207881966.png">

This project begins by computing and plotting Julia sets such that $c = -1$, with $Re(z) ∈ [−2, 2]$ and $Im(z) ∈ [−1, 1]$.
Then we investigate the cycle of different Julia sets, different powers of $z$ and  the maximum number of iterations. We also discuss Julia and Fatou set plots. Julia and Fatou set plots are often colour coded according to how many iterations are required to reach infinity (or whatever large number is approximating infinity). In such a scheme the filled Julia set is black (points never reach infinity). Finally we plot the Mandelbrot - this is the set of all values of $c$ for which the corresponding Julia sets are connected. 
