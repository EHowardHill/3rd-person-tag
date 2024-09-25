import cv2

def list_available_cameras(max_cameras=10):
    """
    Attempts to open each camera index up to max_cameras.
    Returns a list of available camera indices.
    """
    available_cameras = []
    for index in range(max_cameras):
        print(index)
        try:
            cap = cv2.VideoCapture(index)
            if cap is not None and cap.isOpened():
                available_cameras.append(index)
                cap.release()
        except:
            pass
    return available_cameras

if __name__ == "__main__":
    cams = list_available_cameras()
    print(f"Available cameras: {cams}")