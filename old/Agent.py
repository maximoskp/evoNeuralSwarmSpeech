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
        # 18. Closest food location x.
        # 19. Closest food location y.
        # 20. Friend messages (int from bits).
        # 21. Enemy messages (int from bits).
        # 23. Distance from wall x.
        # 24. Distance from wall x.
        self.external_input_size = 24
        # Internal input:
        # 1. Life level.
        # 2. Food level. 
        # 3. Self velocity x.
        # 4. Self velocity y.
        # 5. Self acceleration x.
        # 6. Self acceleration y.
        self.internal_input_size = 6
        # Motion output:
        # 1. Acceleration to current direction (percentage of max, in [-1,1]).
        # 2. Accelerate to average friends location (percentage of max, in [-1,1])
        # 3. Accelerate to closest friend location (percentage of max, in [-1,1])
        # 4. Accelerate to align velocity with friends (what does negative mean?).
        # 5. Accelerate to average enemy location (percentage of max, in [-1,1]).
        # 6. Accelerate to closest enemy location (percentage of max, in [-1,1]).
        # 7. Accelerate to align velocity with enemies (what does negative mean?).
        # 8. Accelerate towards food object (percentage of max, in [-1,1]).
        # 9. Accelerate away from wall (percentage of max, in [-1,1]).
        self.motion_output_size = 8
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
            # eat flag
            'w_eat': np.zeros( self.latent_size ),
            'bias_eat': np.zeros( 1 ),
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
        print('updating friends and enemies', friends, enemies)
    # end update_friends_and_enemies
# end GenericAgent

class PredatorAgent(GenericAgent):
    category = 'predator'
    def __init__(self, genome=None, constants=None, environment=None):
        super().__init__(genome, constants)
    # end init
    
    def update_food_intake( self ):
        print('update food take')
# end PredatorAgent

class PreyAgent(GenericAgent):
    category = 'prey'
    def __init__(self, genome=None, constants=None, environment=None):
        super().__init__(genome, constants)
    # end init
# end PreyAgent