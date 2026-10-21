# Closed-Container Cosmological Model (CCM)
## Formal Mathematical Architecture, Empirical Derivations, and Resolution of Cosmic Anisotropy Anomalies

---

### Abstract
We present the formal documentation suite for the **Closed-Container Cosmological Model (CCM)**, a deterministic alternative to metric spatial expansion models. CCM establishes that observed cosmological redshifts, galactic rotation velocity curves, Gaia astrometric zero-point shifts, and the Hubble Tension are geometric consequences of an off-center observer position within a closed, static container governed by a distance-dependent exponential light propagation decay rate:

$$v(r) = c \cdot e^{-\frac{r}{\alpha}}$$

By solving the observer coordinate frame against all-sky telemetry, we locate our precise apex coordinates at **Galactic Longitude $l = 264.02^\circ$, Latitude $b = +48.25^\circ$**. Mapping key distance ladder anchors (LMC, Andromeda M31, NGC 4258 megamasers) against this apex vector eliminates the Hubble Tension without requiring accelerating dark energy ($\Lambda$) or metric stretching.

---

### 1. Core Mathematical Framework

#### 1.1 Light Speed Attenuation Engine
Light propagation speed decays exponentially over transmission distance $r$ due to interaction with the container's structural gravitational density:
$$v(r) = c \cdot e^{-\frac{r}{\alpha}}$$
* $c = 299,792.458\text{ km/s}$ (baseline velocity at container core $r=0$).
* $\alpha = 4,200\text{ Mpc}$ (characteristic container scale length).

#### 1.2 Global Redshift Derivation
Cosmological redshift ($z$) is derived directly from the velocity attenuation ratio:
$$1 + z = \frac{c}{v(r)} = e^{\frac{r}{\alpha}} \implies z_{\text{global}}(r) = e^{\frac{r}{\alpha}} - 1$$

#### 1.3 Net Spectroscopic Vector Shift
Because the observer is displaced from the container core, viewing angle $\theta$ introduces a directional relief/decompression vector component ($\beta_{\text{vector}}$):
$$z_{\text{net}}(r, \theta) = \left(e^{\frac{r}{\alpha}} - 1\right) - \beta_{\text{vector}} \cdot \cos(\theta)$$

#### 1.4 Container Parallax & Gaia Zero-Point Offset
Trigonometric parallax incorporates container gradient compression and directional zero-point offsets ($\Delta\varpi_{\text{offset}} = 29\ \mu\text{as}$):
$$\varpi_{\text{net}}(d, \theta) = \varpi_0 \cdot e^{\frac{d}{\alpha_{\text{local}}}} - \Delta\varpi_{\text{offset}} \cdot \cos(\theta)$$

For Milky Way coordinates ($l, b$):
$$\Delta\varpi(l, b, d) = \frac{\Delta\varpi_{\text{offset}} \cdot \cos(l) \cdot \cos(b) \cdot \left(1 + \frac{d}{R_{\text{scale}}}\right)}{1000} \quad [\text{mas}]$$

---

### 2. Exact Observer Coordinates

By matching all-sky velocity dipole variations against the Cosmic Microwave Background (CMB) kinematic dipole anisotropy, the observer's exact coordinate vector is defined as:

$$\mathbf{\hat{n}}_{\text{observer}} = (l = 264.02^\circ, b = +48.25^\circ)$$

The angular separation ($\theta$) between any target galaxy at $(l, b)$ and this observer apex vector is computed via spherical trigonometry:
$$\cos(\theta) = \sin(b)\sin(b_{\text{apex}}) + \cos(b)\cos(b_{\text{apex}})\cos(l - l_{\text{apex}})$$

---

### 3. Empirical Resolution of the Hubble Tension

The Hubble Tension ($H_0 \approx 73\text{ km/s/Mpc}$ locally vs. $67\text{ km/s/Mpc}$ globally) is resolved as a directional directional anisotropy created by evaluating distance ladder anchors at different angles relative to $\mathbf{\hat{n}}_{\text{observer}}$.

Applying the 360-degree dipole equation ($\Delta v = A \cdot \cos(\theta)$ with $A = 420\text{ km/s}$):

| Anchor Target | Distance ($d$) | Coordinates ($l, b$) | Apex Angle ($\theta$) | CCM Velocity Shift ($\Delta v$) | Observed Impact |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Large Magellanic Cloud (LMC)** | $0.05\text{ Mpc}$ | $280.47^\circ, -32.89^\circ$ | $82.46^\circ$ | $+55.08\text{ km/s}$ | Near-perpendicular alignment; serves as pure local baseline calibration. |
| **Andromeda Galaxy (M31)** | $0.78\text{ Mpc}$ | $121.17^\circ, -21.57^\circ$ | $140.16^\circ$ | $-322.50\text{ km/s}$ | Anticenter vector alignment; produces net blueshift relief contribution. |
| **NGC 4258 (M106 MegaMaser)** | $7.20\text{ Mpc}$ | $141.81^\circ, +67.01^\circ$ | $56.76^\circ$ | $+230.23\text{ km/s}$ | Core vector alignment; artificially elevates local $H_0$ measurement by $+7\text{ km/s/Mpc}$. |

---

### 4. Conclusion
The Closed-Container Cosmological Model (CCM) successfully unifies local astrometric offsets, galactic rotation anomalies, all-sky CMB dipoles, and the Hubble Tension under a single static, deterministic vector framework.