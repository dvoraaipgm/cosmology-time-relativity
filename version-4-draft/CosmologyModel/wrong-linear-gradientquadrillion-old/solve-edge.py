import numpy as np
from scipy.integrate import solve_ivp

def solve_cosmic_edge():
    # --- 1. Model Parameters ---
    S_target = 365250.0       # The divine-to-human ceiling (scaling ratio)
    n = 1.02                  # Supernova-calibrated 3D curvature exponent
    
    # Characteristic length scale (rough baseline scale in light-years)
    # We test how our ODE derives the exact boundary distance based on this scale.
    R_scale = 5.205e15        # Target light-year scale
    
    # --- 2. Define the Gradient Differential Equation (dS/dr) ---
    # This ODE represents the non-linear rate of change of time dilation 
    # as you move outward through the 3D gravitational well.
    def gradient_ode(r, y):
        S = y[0]
        # Avoid division by zero at the exact center (r = 0)
        if r < 1.0:
            ds_dr = 1e-15
        else:
            # Derivative of the power-law potential profile
            ds_dr = n * (S_target - 1.0) * (r ** (n - 1.0)) / (R_scale ** n)
        return [ds_dr]

    # --- 3. Set Up Event Detector to Catch the Edge ---
    # This event function tells the solver: "Stop immediately when S(r) equals S_target"
    def hit_edge_ceiling(r, y):
        return y[0] - S_target
    
    hit_edge_ceiling.terminal = True     # Stops the integration instantly
    hit_edge_ceiling.direction = 1       # Triggers when crossing upward

    # --- 4. Run the Numerical Integration ---
    # Start at the center (r = 1 ly, S = 1.0) and integrate outward
    r_start = 1.0
    r_end = 1.0e17  # Generous upper bound for the solver search space
    y_initial = [1.0] # Center baseline scaling factor S(0) = 1.0

    print("Integrating non-linear gravitational gradient outward from center...")
    
    solution = solve_ivp(
        fun=gradient_ode,
        t_span=(r_start, r_end),
        y0=y_initial,
        events=hit_edge_ceiling,
        dense_output=True,
        max_step=1e13
    )

    # --- 5. Extract and Display Results ---
    if solution.status == 1 or len(solution.t_events[0]) > 0:
        edge_radius = solution.t_events[0][0]
        final_S = solution.y_events[0][0]
        
        print("\n" + "="*50)
        print("🎉 DYNAMIC COSMIC EDGE SUCCESSFULLY DERIVED!")
        print("="*50)
        print(f"Curvature Exponent (n)       : {n}")
        print(f"Target Scaling Ceiling (S)   : {S_target:,.1f}")
        print(f"Derived Edge Radius (R_edge) : {edge_radius:,.3e} light-years")
        print(f"Final Reached Scaling Factor : {final_S:,.1f}")
        print("="*50)
    else:
        print("Integration completed without hitting the ceiling. Adjust bounds or scale.")

if __name__ == "__main__":
    solve_cosmic_edge()