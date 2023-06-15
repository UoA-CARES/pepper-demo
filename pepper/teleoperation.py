import pygame
import robot


def teleoperate_robot(pepper):
    pygame.init()
    
    print("number of joysticks", pygame.joystick.get_count())
	
    j = pygame.joystick.Joystick(0)
    j.init()

    left_x = 0
    left_y = 0

    right_x = 0
    right_y = 0

    left_trigger = 0
    right_trigger = 0

    button_names = ["A", "B", "X", "Y", "LB", "RB", "BACK", "START", "MENU", "Left", "Right"]

    pepper.set_security_distance(0.01)

    head_yaw_angle = 0
    head_pitch_angle = 0

    button = 0
    RUNNING = True

    awareness_toggle = True
    # pepper.show_map()
    while RUNNING:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                print(event.axis, event.value)
                # Left axis (0, 1)
                if event.axis == 0:
                    if event.value > 0.2 or event.value < -0.2:
                        left_x = event.value
                    else:
                        left_x = 0
                if event.axis == 1:
                    if event.value > 0.2 or event.value < -0.2:
                        left_y = event.value
                    else:
                        left_y = 0
                # Right axis (3, 4)
                if event.axis == 3:
                    if event.value > 0.2 or event.value < -0.2:
                        right_x = event.value
                    else:
                        right_x = 0
                if event.axis == 4:
                    if event.value > 0.1 or event.value < -0.1:
                        right_y = event.value
                    else:
                        right_y = 0
                # Left and right triggers (2, 5)
                if event.axis == 2:
                    if event.value > 0:
                        left_trigger = event.value
                    else:
                        left_trigger = 0
                if event.axis == 5:
                    if event.value > 0:
                        right_trigger = event.value
                    else:
                        right_trigger = 0

                if right_trigger:
                    pepper.move_forward(right_trigger)
                else:
                    pepper.move_forward(-left_trigger)

                if left_x:
                    pepper.turn_around(-left_x)
                
                if left_y:
                    pepper.move_forward(-left_y)

                if right_x:
                    print(right_x)
                    # head_yaw_angle 
                    # pepper.motion_service.setAngles("HeadYaw", -right_x, 0.3)
                if right_y:
                    print(right_y)
                    # pepper.motion_service.setAngles("HeadPitch", right_y, 0.3)
                                
            elif event.type == pygame.JOYBUTTONDOWN:
                print(event.button)
                button = button_names[event.button]
                print(button)
                if button == "MENU":
                    print("Exiting a teleoperation mode")
                    RUNNING = False
                    break
                elif button == 'A':
                    pepper.autonomous_life()
                elif button == 'X':
                    if awareness_toggle:
                        pepper.set_awareness(False)
                    else:
                        pepper.set_awareness(True)
                    awareness_toggle = not(awareness_toggle)
                elif button == 'Y':
                    pepper.mood_happy()

                elif button == 'B':
                    pepper.point_at(1.0, 1.0, 0.0, "RArm", 0)
            
            elif event.type == pygame.JOYHATMOTION:
                if event.value == (1, 0):
                    print('right')
                    if head_yaw_angle > -0.3:
                        head_yaw_angle -= 0.01
                        pepper.motion_service.setAngles("HeadYaw", head_yaw_angle, 0.2)
                elif event.value == (-1, 0):
                    print('left')
                    if head_yaw_angle < 0.3:
                        head_yaw_angle += 0.01
                        pepper.motion_service.setAngles("HeadYaw", head_yaw_angle, 0.2)
                elif event.value == (0, 1):
                    print('up')
                    if head_pitch_angle > -0.3:
                        head_pitch_angle -= 0.01
                        pepper.motion_service.setAngles("HeadPitch", head_pitch_angle, 0.2)
                elif event.value == (0, -1):
                    print('down')
                    if head_pitch_angle < 0.3:
                        head_pitch_angle += 0.01
                        pepper.motion_service.setAngles("HeadPitch", head_pitch_angle, 0.2)
                    