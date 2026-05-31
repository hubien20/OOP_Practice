class AudioLesson:
    def __init__(self, id: int, title: str, level: str, total_duration: int, segments: list = None):
        self.id = id
        self.title = title
        self.level = level
        self.total_duration = total_duration
        # Nếu không truyền vào danh sách segment, mặc định sẽ tạo một danh sách rỗng
        self.segments = segments if segments is not None else []
        
    # Bạn có thể thêm các phương thức getter/setter hoặc quản lý segment nếu cần:
    def add_segment(self, segment):
        self.segments.append(segment)