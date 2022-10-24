#%% imports
from scipy.spatial.distance import pdist, squareform
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

#%% functions
def create_mat(df):
    print("building matrix")
    mat = pdist(locations)
    return squareform(mat)

def create_distance_callback(dist_matrix):
    def distance_callback(from_node, to_node):
      return int(dist_matrix[from_node][to_node])
    return distance_callback

status_dict = {0: 'ROUTING_NOT_SOLVED', 
               1: 'ROUTING_SUCCESS', 
               2: 'ROUTING_FAIL',
               3: 'ROUTING_FAIL_TIMEOUT',
               4: 'ROUTING_INVALID'}

def optimize(df, startnode=None, stopnode=None, fixed=False):     
    num_nodes = df.shape[0]
    mat = create_mat(df)
    dist_callback = create_distance_callback(mat)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
#     search_parameters.time_limit_ms = int(1000*60*numminutes)
    search_parameters.solution_limit = num_iters 
    search_parameters.first_solution_strategy = (
                                    routing_enums_pb2.FirstSolutionStrategy.SAVINGS)
    search_parameters.local_search_metaheuristic = (
                            routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)

    if fixed:
        routemodel = pywrapcp.RoutingModel(num_nodes, 1, [startnode], [stopnode])
    else:
        routemodel = pywrapcp.RoutingModel(num_nodes, 1, startnode)
    routemodel.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    
    print("optimizing {} cities".format(num_nodes)) 
    assignment = routemodel.SolveWithParameters(search_parameters)

    print("status: ", status_dict.get(routemodel.status()))
    print("travel distance: ",  str(assignment.ObjectiveValue()), "\n")
    return routemodel, assignment
    
def get_route(df, startnode, stopnode, fixed): 
    routemodel, assignment = optimize(df, int(startnode), int(stopnode), fixed)
    route_number = 0
    node = routemodel.Start(route_number)
    route = []
    while not routemodel.IsEnd(node):
        route.append(node) 
        node = assignment.Value(routemodel.NextVar(node))
    return route
