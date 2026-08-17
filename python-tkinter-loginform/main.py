import customtkinter as ctk
from PIL import Image


# ==========================================
# APP CONFIGURATION
# ==========================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# ==========================================
# MAIN WINDOW
# ==========================================

app = ctk.CTk()

app.title("Facebook Login")
app.geometry("900x600")
app.resizable(False, False)

app.configure(fg_color="#f0f2f5")


# ==========================================
# USER ACCOUNT
# ==========================================

user_email = ""
user_password = ""


# ==========================================
# LOAD GIF BACKGROUND
# ==========================================

gif = Image.open("assets/facebook_bg.gif")

gif_frames = []

try:
    while True:

        frame = gif.copy().convert("RGB")

        frame = frame.resize(
            (900, 600),
            Image.Resampling.LANCZOS
        )

        gif_frames.append(frame)

        gif.seek(gif.tell() + 1)

except EOFError:
    pass


# ==========================================
# BACKGROUND LABEL
# ==========================================

background_label = ctk.CTkLabel(
    app,
    text="",
    width=900,
    height=600
)

background_label.place(
    x=0,
    y=0
)


# ==========================================
# ANIMATE GIF
# ==========================================

def animate_gif(frame_index=0):

    frame = gif_frames[frame_index]

    background_image = ctk.CTkImage(
        light_image=frame,
        dark_image=frame,
        size=(900, 600)
    )

    background_label.configure(
        image=background_image
    )

    # Keep reference to the image
    background_label.image = background_image

    # Move to the next frame
    next_frame = (frame_index + 1) % len(gif_frames)

    # Animation speed
    app.after(
        100,
        animate_gif,
        next_frame
    )


# Start GIF
animate_gif()


# ==========================================
# LEFT SIDE CONTENT
# ==========================================

left_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

left_frame.place(
    relx=0.08,
    rely=0.25
)


# ==========================================
# FACEBOOK LOGO
# ==========================================

facebook_label = ctk.CTkLabel(
    left_frame,
    text="facebook",
    font=ctk.CTkFont(
        family="Arial",
        size=48,
        weight="bold"
    ),
    text_color="#1877F2"
)

facebook_label.pack(
    anchor="w"
)


# ==========================================
# DESCRIPTION
# ==========================================

description_label = ctk.CTkLabel(
    left_frame,
    text="Connect with friends and the world\n"
         "around you on Facebook.",
    font=ctk.CTkFont(
        family="Arial",
        size=20
    ),
    text_color="#1c1e21",
    justify="left"
)

description_label.pack(
    pady=(5, 0),
    anchor="w"
)


# ==========================================
# LOGIN CARD
# ==========================================

login_card = ctk.CTkFrame(
    app,
    width=380,
    height=370,
    corner_radius=10,
    fg_color="white"
)

login_card.place(
    relx=0.67,
    rely=0.48,
    anchor="center"
)


# ==========================================
# EMAIL ENTRY
# ==========================================

email_entry = ctk.CTkEntry(
    login_card,
    width=330,
    height=50,
    corner_radius=6,
    placeholder_text="Email or phone number",
    font=ctk.CTkFont(size=15),
    border_width=1,
    border_color="#dddfe2"
)

email_entry.place(
    x=25,
    y=25
)


# ==========================================
# PASSWORD ENTRY
# ==========================================

password_entry = ctk.CTkEntry(
    login_card,
    width=330,
    height=50,
    corner_radius=6,
    placeholder_text="Password",
    show="•",
    font=ctk.CTkFont(size=15),
    border_width=1,
    border_color="#dddfe2"
)

password_entry.place(
    x=25,
    y=85
)


# ==========================================
# MESSAGE LABEL
# ==========================================

message_label = ctk.CTkLabel(
    login_card,
    text="",
    font=ctk.CTkFont(
        size=13
    )
)

message_label.place(
    x=25,
    y=325
)


# ==========================================
# LOGIN FUNCTION
# ==========================================

def login():

    global user_email, user_password

    email = email_entry.get().strip()
    password = password_entry.get()

    # Check empty fields
    if email == "" or password == "":
        message_label.configure(
            text="Please enter your email and password.",
            text_color="red"
        )

    # Check if account exists
    elif user_email == "":
        message_label.configure(
            text="No account exists. Create an account first.",
            text_color="red"
        )

    # Check credentials
    elif email == user_email and password == user_password:

        message_label.configure(
            text="Login successful!",
            text_color="green"
        )

    else:

        message_label.configure(
            text="Incorrect email or password.",
            text_color="red"
        )


# ==========================================
# LOGIN BUTTON
# ==========================================

login_button = ctk.CTkButton(
    login_card,
    width=330,
    height=50,
    corner_radius=6,
    text="Log In",
    font=ctk.CTkFont(
        size=18,
        weight="bold"
    ),
    fg_color="#1877F2",
    hover_color="#166FE5",
    command=login
)

login_button.place(
    x=25,
    y=150
)


# ==========================================
# FORGOTTEN PASSWORD
# ==========================================

def forgot_password():

    message_label.configure(
        text="Password recovery is not available yet.",
        text_color="#1877F2"
    )


forgot_button = ctk.CTkButton(
    login_card,
    text="Forgotten password?",
    fg_color="transparent",
    hover_color="#f5f5f5",
    text_color="#1877F2",
    font=ctk.CTkFont(
        size=14
    ),
    command=forgot_password
)

forgot_button.place(
    x=100,
    y=205
)


# ==========================================
# DIVIDER
# ==========================================

divider = ctk.CTkFrame(
    login_card,
    width=330,
    height=1,
    fg_color="#dadde1"
)

divider.place(
    x=25,
    y=250
)


# ==========================================
# CREATE ACCOUNT FUNCTION
# ==========================================

def create_account():

    global user_email, user_password

    email = email_entry.get().strip()
    password = password_entry.get()

    # Check empty fields
    if email == "" or password == "":

        message_label.configure(
            text="Enter an email and password first.",
            text_color="red"
        )

        return

    # Check email
    if "@" not in email or "." not in email:

        message_label.configure(
            text="Please enter a valid email address.",
            text_color="red"
        )

        return

    # Check password length
    if len(password) < 6:

        message_label.configure(
            text="Password must be at least 6 characters.",
            text_color="red"
        )

        return

    # Check if account already exists
    if user_email != "":

        message_label.configure(
            text="An account already exists.",
            text_color="red"
        )

        return

    # Save account
    user_email = email
    user_password = password

    message_label.configure(
        text="Account created! You can now log in.",
        text_color="green"
    )

    # Clear input fields
    email_entry.delete(
        0,
        "end"
    )

    password_entry.delete(
        0,
        "end"
    )


# ==========================================
# CREATE ACCOUNT BUTTON
# ==========================================

create_account_button = ctk.CTkButton(
    login_card,
    width=180,
    height=45,
    corner_radius=6,
    text="Create new account",
    font=ctk.CTkFont(
        size=15,
        weight="bold"
    ),
    fg_color="#42b72a",
    hover_color="#36a420",
    command=create_account
)

create_account_button.place(
    x=100,
    y=270
)


# ==========================================
# START APPLICATION
# ==========================================

app.mainloop()