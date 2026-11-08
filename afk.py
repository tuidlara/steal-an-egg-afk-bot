import time
import pydirectinput as pdi

INTERVAL = 5
LEFT_DURATION = 0.08
JUMP_DURATION = 0.3
START_DELAY = 5


def move_character():
    print("Jumping...")
    pdi.keyDown("space")
    time.sleep(JUMP_DURATION)
    pdi.keyUp("space")

    time.sleep(1)

    print("Moving left...")
    pdi.keyDown("a")
    time.sleep(LEFT_DURATION)
    pdi.keyUp("a")

    print("Cycle completed!")


def main():
    print(f"Starting in {START_DELAY} seconds...")
    time.sleep(START_DELAY)

    try:
        while True:
            time.sleep(INTERVAL)
            move_character()

    except KeyboardInterrupt:
        print("\nScript stopped.")


if __name__ == "__main__":
    main()
