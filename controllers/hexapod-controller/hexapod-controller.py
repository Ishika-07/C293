from controller import Robot

robot = Robot()
timestep = 32

motor_RPC = robot.getDevice("RPC")
motor_RPF = robot.getDevice("RPF")

motor_RMC = robot.getDevice("RMC")
motor_RMF = robot.getDevice("RMF")

motor_RAC = robot.getDevice("RAC")
motor_RAF = robot.getDevice("RAF")

motor_LPC = robot.getDevice("LPC")
motor_LPF = robot.getDevice("LPF")

motor_LMC = robot.getDevice("LMC")
motor_LMF = robot.getDevice("LMF")

motor_LAC = robot.getDevice("LAC")
motor_LAF = robot.getDevice("LAF")

