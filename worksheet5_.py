import numpy as np

try:
    from scipy import stats, fftpack, interpolate, optimize, signal
    from scipy.integrate import odeint
except Exception as e:
    print("SciPy import failed:", e)

import matplotlib.pyplot as plt

def q1_random_stats(n=1000):
    arr = np.random.randn(n)
    mean = arr.mean()
    median = np.median(arr)
    var = arr.var()
    return arr, mean, median, var

def q2_fft_2d():
    a = np.random.rand(8,8)
    A = fftpack.fft2(a)
    return a, A

def q3_linear_algebra():
    M = np.array([[4,2,1],[0,3,-1],[1,0,2]], dtype=float)
    det = np.linalg.det(M)
    inv = np.linalg.inv(M)
    eigvals, eigvecs = np.linalg.eig(M)
    return M, det, inv, eigvals, eigvecs

def q4_interpolation():
    x = np.linspace(0, 10, 10)
    y = np.sin(x) + 0.1*np.random.randn(x.size)
    f = interpolate.interp1d(x, y, kind='cubic')
    xi = np.linspace(0,10,200)
    yi = f(xi)
    return x, y, xi, yi

def q5_signal_filter():
    t = np.linspace(0,1,500)
    data = np.sin(2*np.pi*5*t) + 0.5*np.random.randn(t.size)
    b, a = signal.butter(4, 0.1)  
    filtered = signal.filtfilt(b,a,data)
    return t, data, filtered

def q6_sales_simulation():
    
    sales = np.random.randint(50,500,size=(12,4))
    total_sales = sales.sum()
    avg_sales = sales.mean()
    max_sales = sales.max()
    best_month = sales.sum(axis=1).argmax()+1
    worst_month = sales.sum(axis=1).argmin()+1
    return sales, total_sales, avg_sales, max_sales, best_month, worst_month

def q7_marks_analysis():
    names = ["Arin","Aditya","Chirag","Gurleen","Kunal"]
    marks = np.array([[85,78,92,88],
                      [79,82,74,90],
                      [90,85,89,92],
                      [66,75,80,78],
                      [70,68,75,85]])
    totals = marks.sum(axis=1)
    averages = marks.mean(axis=1)
    subject_perf = marks.mean(axis=0)
    topper = names[totals.argmax()]
    bottom = names[totals.argmin()]
    passing = (marks >= 40).all(axis=1).mean()*100  
    return names, marks, totals, averages, subject_perf, topper, bottom, passing

def q8_curve_fit_velocity():
    t = np.array([0,1,2,3,4,5])
    v = np.array([2,3.1,7.9,18.2,34.3,56.2])
    def quad(t,a,b,c): return a*t**2 + b*t + c
    popt, pcov = optimize.curve_fit(quad, t, v)
    
    tfine = np.linspace(t.min(), t.max(), 200)
    vf = quad(tfine, *popt)
    return t, v, tfine, vf, popt

def q9_marks_plotting():
    
    names, marks, totals, *_ = q7_marks_analysis()
   
    return names, marks, totals

def q10_plot_quadratic_fit():
    return q8_curve_fit_velocity()

def q11_population_regression():
    years = np.array([2000,2005,2010,2015,2020])
    pop = np.array([50,55,70,80,90])
    slope, intercept, r, p, se = stats.linregress(years, pop)
    pop_2008 = intercept + slope*2008
    
    f = interpolate.interp1d(years, pop, kind='linear')
    pop_2008_i = float(f(2008))
    return slope, intercept, r, pop_2008, pop_2008_i

def q12_poly_roots_and_plot():
    # p(x) = 3x^3 -5x^2 +2x -8
    coeffs = [3, -5, 2, -8]
    roots = np.roots(coeffs)
    x = np.linspace(-3,3,400)
    p = np.poly1d(coeffs)
    y = p(x)
    return roots, x, y

def q13_performance_compare():
    import time
    sizes_mb = [200,400,600,800,1000]
    results = {}
    for mb in sizes_mb:
        
        s = ("abcde " * 1024) * (mb//1)  
        t0 = time.time()
        _ = s.upper()
        t1 = time.time()
        results[mb] = t1 - t0
    return results

def q14_local_minima():
    def f(x): return x**4 - 3*x**3 + 2
    
    xs = np.linspace(-2,3,100)
    roots = []
    minima = []
    for x0 in np.linspace(-2,3,6):
        try:
            res = optimize.minimize(f, x0)
            if res.success:
                minima.append((res.x[0], res.fun))
        except:
            pass
    return minima, xs, [f(x) for x in xs]

def q15_damped_oscillator():
    
    
    m = 1.0
    k = 4.0      
    c = 0.4      
    omega_n = np.sqrt(k/m)
    def deriv(y, t):
        theta, omega = y
        dtheta = omega
        domega = -(c/m)*omega - (k/m)*theta
        return [dtheta, domega]
    t = np.linspace(0,20,1000)
    y0 = [1.0, 0.0]
    sol = odeint(deriv, y0, t)
    theta = sol[:,0]
    max_disp = theta.max()
    time_of_max = t[theta.argmax()]
    return t, theta, max_disp, time_of_max

if __name__ == "__main__":
    print("Q1 stats:", q1_random_stats(500)[1:])
    print("Q2 fft shape:", q2_fft_2d()[1].shape)
    print("Q3:", q3_linear_algebra()[:2])
    print("Q4 interpolation sample:", q4_interpolation()[0:2])
    print("Q6 sales:", q6_sales_simulation()[1:4])
    print("Q8 popt:", q8_curve_fit_velocity()[4])
    print("Q11 regression:", q11_population_regression())
    print("Q12 roots:", q12_poly_roots_and_plot()[0])
    print("Q15 damped oscillator max:", q15_damped_oscillator()[2:])
