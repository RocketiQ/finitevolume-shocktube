# Methods (finitevolume-shocktube)

**Equations:** 1D compressible Euler (ρ, ρu, ρE), γ=1.4.  
**Flux:** Roe approximate Riemann solver with Roe-averaged state; eigenvalues λ = u ± a, u.  
**Initial condition (Sod):** Left (ρ=1, u=0, p=1), Right (ρ=0.125, u=0, p=0.1).  
**Time step:** CFL-based dt = CFL * dx / max(|u| + a).  
**BCs:** Dirichlet ends (frozen).  
**Notes:** Positivity check; conservation verified approximately in tests.
