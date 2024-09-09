import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import subprocess
import os

def open_program1():
    subprocess.Popen(['python', '55.py'])
    #เปิดโปรแกรม 1 ซ้อนทับเลยทันที แล้วเมื่อปิดโปรแกรม 1 จะกลับมาที่หน้าต่างหลัก
    root.deiconify()

def open_program2():
    subprocess.Popen(['python', 'adgender.py'])
    #เปิดโปรแกรม 2 ซ้อนทับเลยทันที แล้วเมื่อปิดโปรแกรม 2 จะกลับมาที่หน้าต่างหลัก
    root.deiconify()
    
def exit_program():
    root.destroy()

def update_animation(frame_index):
    frame = frames[frame_index]
    photo = ImageTk.PhotoImage(frame)
    label_animation.config(image=photo)
    label_animation.image = photo
    root.after(100, update_animation, (frame_index + 1) % len(frames))

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Main Menu")

# ตั้งค่าหน้าต่างให้เต็มจอ
root.attributes('-fullscreen', True)

# เปลี่ยนสีพื้นหลังหน้าต่างเป็นสีดํา
root.configure(bg='#2E2E2E')

# สร้างกรอบหลักสำหรับจัดการกับ layout
main_frame = tk.Frame(root, bg='#2E2E2E')
main_frame.pack(expand=True, fill='both')

# ข้อความต้อนรับ
welcome_message = tk.Label(main_frame, text="Welcome to the AI Program Main Menu !", font=("Helvetica", 18), bg='#2E2E2E', fg='white')
welcome_message.pack(pady=20)
#เพิ่มเส้นแบ่ง
separator1 = tk.Frame(main_frame, height=2, bd=1, relief=tk.SUNKEN, bg='#2E2E2E')
separator1.pack(fill='x', padx=20, pady=10)
# ข้อความคำแนะนำ
instruction_message = tk.Label(main_frame, text="Please select the program you want to open", font=("Helvetica", 14), bg='#2E2E2E', fg='white')
instruction_message.pack(pady=10)


# โหลดไฟล์ GIF แอนิเมชั่น
gif_path = "ai.gif"
gif_image = Image.open(gif_path)
frames = [frame.copy() for frame in ImageSequence.Iterator(gif_image)]

#ปรับขนาดของแอนิเมชั่น
frames = [frame.resize((250, 250), Image.LANCZOS) for frame in frames]

# สร้าง Label สำหรับแสดงแอนิเมชั่น
label_animation = tk.Label(main_frame, bg='#2E2E2E')
label_animation.pack(pady=20)

# เริ่มแอนิเมชั่น
update_animation(0)

# สร้างกรอบย่อยสำหรับโปรแกรม 1
frame_program1 = tk.Frame(main_frame, bg='#2E2E2E')
frame_program1.pack(side='left', padx=20, pady=20, expand=True)

# โหลดและแสดงรูปภาพสำหรับโปรแกรม 1
img1 = Image.open("p1.png")
img1 = img1.resize((550, 550), Image.LANCZOS)
img1 = ImageTk.PhotoImage(img1)
label_img1 = tk.Label(frame_program1, image=img1, bg='#2E2E2E')

# ปุ่มเปิดโปรแกรม 1
btn_program1 = tk.Button(frame_program1, text="Open AI Qr-Code Scanner Program ", command=open_program1, bg='#b62f72', fg='white', font=("Helvetica", 12))

btn_program1.pack(pady=10)
label_img1.pack(pady=10)

# สร้างกรอบย่อยสำหรับโปรแกรม 2
frame_program2 = tk.Frame(main_frame, bg='#2E2E2E')
frame_program2.pack(side='right', padx=20, pady=20, expand=True)

# โหลดและแสดงรูปภาพสำหรับโปรแกรม 2
img2 = Image.open("p2.png")
img2 = img2.resize((550, 550), Image.LANCZOS)
img2 = ImageTk.PhotoImage(img2)
label_img2 = tk.Label(frame_program2, image=img2, bg='#2E2E2E')

# ปุ่มเปิดโปรแกรม 2
btn_program2 = tk.Button(frame_program2, text="Open AI AD Gender Selection Program ", command=open_program2, bg='#b62f72', fg='white', font=("Helvetica", 12))

btn_program2.pack(pady=10)
label_img2.pack(pady=10)

# หัวข้อผู้พัฒนา 
# สร้างกรอบข้อความสวยๆ
text_frame = tk.Frame(main_frame, bg='#2E2E2E', bd=2, relief=tk.RAISED)
text_frame.pack(pady=20)
# ข้อความในกรอบ
developer_title = tk.Label(text_frame, text="Developer Information", font=("Helvetica", 14), bg='#2E2E2E', fg='white')
developer_title.pack(pady=10)
# เพิ่มเส้นแบ่ง
separator = tk.Frame(main_frame, height=2, bd=1, relief=tk.SUNKEN, bg='#2E2E2E')
separator.pack(fill='x', padx=20, pady=10)

#เพิ่มรูปของผู้พัฒนา
img3 = Image.open("pic.png")
img3 = img3.resize((100, 100), Image.LANCZOS)
img3 = ImageTk.PhotoImage(img3)
label_img3 = tk.Label(main_frame, image=img3, bg='#2E2E2E')
label_img3.pack(pady=10)
# ข้อมูลผู้พัฒนา
developer_info = tk.Label(main_frame, text=" Mr. Patchara Al-umaree\n\nCode: 6651630177\n\nEmail: Patcharaalumaree@gmail.com", font=("Helvetica", 12), bg='#2E2E2E', fg='white')
developer_info.pack(pady=20)
# เพิ่มรูปเกรด
img4 = Image.open("mygrade.png")
img4 = img4.resize((100, 100), Image.LANCZOS)
img4 = ImageTk.PhotoImage(img4)
label_img4 = tk.Label(main_frame, image=img4, bg='#2E2E2E')
label_img4.pack(pady=10)

btn_github = tk.Button(main_frame, text="GitHub", command=lambda: subprocess.Popen(['start', 'https://github.com/MrPatchara'], shell=True), bg='#674ea7', fg='white', font=("Helvetica", 14))
btn_github.pack(pady=10)

# เพิ่มเส้นแบ่ง
separator2 = tk.Frame(main_frame, height=2, bd=1, relief=tk.SUNKEN, bg='#2E2E2E')
separator2.pack(fill='x', padx=20, pady=10)

# ปุ่ม Exit
exit_button = tk.Button(main_frame, text="Exit", command=exit_program, bg='#D32F2F', fg='white', font=("Helvetica", 14))
exit_button.pack(pady=10)

# เริ่มการทำงานของ GUI
root.mainloop()
