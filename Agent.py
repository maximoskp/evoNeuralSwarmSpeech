import numpy as np
import auxilliary_functions as aux

class GenericAgent:
    category = 'generic'
    def __init__(self, genome=None, constants=None, environment=None):
        # External input:
        # 1. Number of friends.
        # 2. Average of friends location x.
        # 3. Average of friends location y.
        # 4. Closest friend location x.
        # 5. Closest friend location y.
        # 6. Average velocity of friends x.
        # 7. Average velocity of friends y.
        # 8. Closest friend velocity x.
        # 9. Closest friend velocity y.
        # 10. Number of enemies.
        # 11. Average of enemies location x.
        # 12. Average of enemies location y.
        # 13. Closest enemy location.
        # 14. Average velocity of enemies x.
        # 15. Average velocity of enemies y.
        # 16. Closest enemy velocity x.
        # 17. Closest enemy velocity y.
        # 18. Friend loudest messages (int from bits).
        # 19. Enemy loudest messages (int from bits).
        # 20. Distance from wall x.
        # 21. Distance from wall x.
        self.external_input_size = 21
        # Internal input:
        # 1. Life level.
        # 2. Self velocity x.
        # 3. Self velocity y.
        # 4. Self acceleration x.
        # 5. Self acceleration y.
        self.internal_input_size = 5
        # Motion output:
        # 1. Accelerate to average friends location (percentage of max, in [-1,1])
        # 2. Accelerate to closest friend location (percentage of max, in [-1,1])
        # 3. Accelerate to align velocity with friends (what does negative mean?).
        # 4. Accelerate to average enemy location (percentage of max, in [-1,1]).
        # 5. Accelerate to closest enemy location (percentage of max, in [-1,1]).
        # 6. Accelerate to align velocity with enemies (what does negative mean?).
        # 7. Accelerate away from wall (percentage of max, in [-1,1]).
        self.motion_output_size = 7
        # speech information
        self.speech_bits = 4
        # WEIGHTS
        self.latent_size = 10
        self.init_weights_zero()
        # genome
        if genome is None:
            self.random_genome()
        else:
            self.genome = genome
            self.genome_size = self.genome.size
        self.genome2weights()
        # all constants
        self.get_constants(constants)
        self.environment = environment
        # position, velocity and acceleration
        self.init_random()
        self.is_alive = True
        self.food_level = self.constances.agent_constants[self.category]['food_level']
    # end __init__

    def init_weights_zero(self):
        self.weights = {
            # input to latent
            'w_in': np.zeros( (self.internal_input_size + self.external_input_size , self.latent_size) ),
            'bias_in': np.zeros( self.latent_size ),
            # latent to:
            # spoken message
            'w_speech': np.zeros( (self.latent_size , self.speech_bits) ),
            'bias_speech': np.zeros( self.speech_bits ),
            # motion weights
            'w_motion': np.zeros( (self.latent_size , self.motion_output_size) ),
            'bias_motion': np.zeros( self.motion_output_size )
        }
        self.weight_keys = self.weights.keys()
    # def end init_weights_zero

    def random_genome(self):
        self.genome_size = 0
        for k in self.weight_keys:
            self.genome_size += self.weights[k].size
        self.genome = 2*np.random.random( self.genome_size ) - 1
    # end random_genome

    def genome2weights(self):
        cutoff = 0
        for k in self.weight_keys:
            self.weights[k] = np.reshape( self.genome[cutoff:cutoff+self.weights[k].size] , self.weights[k].shape )
    # end genome2weights

    def get_constants(self, constants):
        self.constants = constants
    # end get_category_constants

    def init_random(self):
        # position
        self.x = np.random.rand()*self.constants.world_width
        self.y = np.random.rand()*self.constants.world_height
        # velocity
        vx = 2*np.random.rand() - 1
        vy = 2*np.random.rand() - 1
        self.vx , self.vy = aux.limit_xy( vx, vy, self.constants.agent_constants[self.category]['velocity_limit'] )
        # acceleration
        ax = 2*np.random.rand() - 1
        ay = 2*np.random.rand() - 1
        self.ax , self.ay = aux.limit_xy( ax, ay, self.constants.agent_constants[self.category]['acceleration_limit'] )
    # end init_random_position_velocity

    def update_friends_and_enemies( self, friends=None, enemies=None ):
        # friends
        perceived_friends = []
        self.perceived_friends_mean_location = []
        closest_friend_distance = np.inf
        self.closest_friend_location = []
        for f in self.friends:
            if aux.dist_2d_arrays( [self.x, self.y], [f.x, f.y] ) < self.constances.agent_constants[self.category]['perception_radius'] :
                perceived_friends.append( [f.x, f.y] )
            if aux.dist_2d_arrays( [self.x, self.y], [f.x, f.y] ) < closest_friend_distance:
                self.closest_friend_location = [f.x, f.y]
                closest_friend_distance = aux.dist_2d_arrays( [self.x, self.y], [f.x, f.y] )
        if len( perceived_friends ) > 0:
            self.perceived_friends_mean_location = np.mean( np.array( perceived_friends ), axis=0 )
        else:
            self.perceived_friends_mean_location = np.array( [self.x, self.y] )
        # TODO: get loudest message of friends
        # enemies
        perceived_enemies = []
        self.perceived_enemies_mean_location = []
        closest_enemy_distance = np.inf
        self.closest_enemy = None
        for f in self.enemies:
            if aux.dist_2d_arrays( [self.x, self.y], [f.x, f.y] ) < self.constances.agent_constants[self.category]['perception_radius'] :
                perceived_enemies.append( [f.x, f.y] )
            if aux.dist_2d_arrays( [self.x, self.y], [f.x, f.y] ) < closest_enemy_distance:
                self.closest_enemy = f
                closest_enemy_distance = aux.dist_2d_arrays( [self.x, self.y], [f.x, f.y] )
        if len( perceived_enemies ) > 0:
            self.perceived_enemies_mean_location = np.mean( np.array( perceived_enemies ), axis=0 )
        else:
            self.perceived_enemies_mean_location = np.array( [np.inf, np.inf] )
        # TODO: get loudest message of enemies
    # end update_friends_and_enemies
    
    def move(self):
        print('here s the money')
    # end move
    
    def update_food( self ):
        print('to be overriden')
    # end update_food
# end GenericAgent

class PredatorAgent(GenericAgent):
    category = 'predator'
    def __init__(self, genome=None, constants=None, environment=None):
        super().__init__(genome, constants)
    # end init
    
    def update_food( self ):
        self.food_level -= self.constances.agent_constants[self.category]['food_depletion']
        agents2die = {
            'predator': [],
            'prey': []
        }
        if self.food_level < 0:
            self.is_alive = False
            agents2die['predator'].append(self)
        if self.is_alive and aux.dist_2d_arrays( [self.x, self.y], self.closest_enemy_location[0]) < self.constances.agent_constants[self.category]['food_radius'] and self.food_level < self.constances.agent_constants[self.category]['food_level']/2 :
            self.food_level = self.constances.agent_constants[self.category]['food_level']
            agents2die['prey'].append(self.closest_enemy)
        return agents2die
    # end update_food
# end PredatorAgent

class PreyAgent(GenericAgent):
    category = 'prey'
    def __init__(self, genome=None, constants=None, environment=None):
        super().__init__(genome, constants)
    # end init
# end PreyAgent