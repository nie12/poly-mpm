from grid import Grid
from mplist import MatPointList
from numpy import array, pi, zeros, ones

def get_parameters(params):
    input_file = 'from inputs.' + params[0] +' import Params'
    exec(input_file, globals())
    P = Params(params) # Initialise parameters from input file

    if not hasattr(P, 't'): P.t = 0. # physical time (s)
    if not hasattr(P, 'tstep'): P.tstep = 0
    if not hasattr(P, 'grid_save'): P.grid_save = 0 # save counter
    if not hasattr(P, 'mp_save'): P.mp_save = 0 # save counter
    if not hasattr(P, 'M_tol'): P.M_tol = 1e-10 # very small mass (kg)
    if not hasattr(P, 'nt'): P.nt = int(P.t_f/P.dt) # number of timesteps
    if not hasattr(P, 'max_g'): P.max_g = 0.
    if not hasattr(P, 'max_q'): P.max_q = 0.
    if not hasattr(P, 'g'): P.g = P.max_g#array([0,0,0])
    if not hasattr(P, 'q_v'): P.q_v = P.max_q#array([0,0,0])
    if not hasattr(P, 'q_h'): P.q_h = P.max_q#array([0,0,0])
    if not hasattr(P, 'has_yielded'): P.has_yielded = False
    if not hasattr(P, 'damping'): P.damping = False
    if not hasattr(P, 'theta'): P.theta = 0. # vertical
    if not hasattr(P, 'pressure'): P.pressure = None # lithostatic
    if not hasattr(P, 'segregate_mp'): P.segregate_mp = False # NEVER USE THIS!!!
    if not hasattr(P, 'segregate_grid'): P.segregate_grid = False
    if not hasattr(P, 'initial_flow'): P.initial_flow = False # give initial velocities which correspond to 1D steady state
    if not hasattr(P, 'smooth_grad2'): P.smooth_grad2 = False # use artifical smoothing on calculation of the gradient of the shear strain rate


    if not hasattr(P.B, 'wall'): P.B.wall = False
    if not hasattr(P.B, 'roughness'): P.B.roughness = False
    if not hasattr(P.B, 'no_slip_bottom'): P.B.no_slip_bottom = False
    if not hasattr(P.B, 'cyclic_lr'): P.B.cyclic_lr = False
    if not hasattr(P.B, 'has_top'): P.B.has_top = False
    if not hasattr(P.B, 'has_bottom'): P.B.has_bottom = False
    if not hasattr(P.B, 'has_right'): P.B.has_right = False
    if not hasattr(P.B, 'has_left'): P.B.has_left = False
    if not hasattr(P.B, 'box'): P.B.box = False
    if not hasattr(P.B, 'outlet_left'): P.B.outlet_left = False
    if not hasattr(P.B, 'outlet_bottom'): P.B.outlet_bottom = False
    if not hasattr(P.B, 'inlet_right'): P.B.inlet_right = False
    if not hasattr(P.B, 'force_boundaries'): P.B.force_boundaries = False
    if not hasattr(P.B, 'vertical_force'): P.B.vertical_force = False
    if not hasattr(P.B, 'horizontal_force'): P.B.horizontal_force = False
    if not hasattr(P.B, 'conveyor'): P.B.conveyor = False
    if not hasattr(P.B, 'silo_left'): P.B.silo_left = False
    if not hasattr(P.B, 'silo_bottom'): P.B.silo_bottom = False

    if not hasattr(P.G, 'thickness'): P.G.thickness = 1. # (m) into page
    if not hasattr(P.G, 'ns'): P.G.ns = 1 # number of grain sizes
    if not hasattr(P.G, 's'): P.G.s = [0.001] # 1mm grain size by default (m)
    if not hasattr(P.G, 's_m'): P.G.s_m = min(P.G.s)
    if not hasattr(P.G, 's_M'): P.G.s_M = max(P.G.s)

    if type(P.S) is not list: P.S = [P.S] # if just one phase, still turn into a list
    P.phases = len(P.S)
    for p in range(P.phases):
        # if not hasattr(P.S[p], 'phi'): P.S[p].phi = [1.]
        if not hasattr(P.S[p], 'phi'): P.S[p].phi = ones([P.G.ns])/float(P.G.ns)

    if not hasattr(P.O, 'check_positions'): P.O.check_positions = False
    if not hasattr(P.O, 'measure_stiffness'): P.O.measure_stiffness = False
    if not hasattr(P.O, 'measure_energy'): P.O.measure_energy = False
    if not hasattr(P.O, 'plot_gsd_mp'): P.O.plot_gsd_mp = False
    if not hasattr(P.O, 'plot_gsd_grid'): P.O.plot_gsd_grid = False
    if not hasattr(P.O, 'plot_material_points'): P.O.plot_material_points = False
    if not hasattr(P.O, 'plot_continuum'): P.O.plot_continuum = False
    if not hasattr(P.O, 'save_s_bar'): P.O.save_s_bar = False
    if not hasattr(P.O, 'save_u'): P.O.save_u = False

    if P.O.measure_energy: P.O.energy = zeros((P.nt+1,4)) # energy
    P.mode = params[0]
    P.update_forces()
    G = Grid(P) # Initialise grid
    L = MatPointList(P,G) # Initialise material point list storage
    return P,G,L

if __name__ == '__main__':
    P,G,L = get_parameters(params)
