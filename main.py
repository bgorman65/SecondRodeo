from Contractor import Contractor
from Calf import Calf
from Steer import Steer
from Bull import Bull
from Bronc import Bronc
from Database import Database
import customtkinter as ctk


# Class to make the ContractorFrame
class ContractorFrame(ctk.CTkFrame):

    # Constructor
    def __init__(self, parent, database):
        super().__init__(parent, height=100, width=600, border_color="black", border_width=2)
        self._set_appearance_mode("dark")

        # Getting the database object
        self.database = database

        # Creating the widgets
        self.top_label = ctk.CTkLabel(self, text="Add Contractor")
        self.top_label._set_appearance_mode("dark")
        self.top_label.pack(side=ctk.LEFT, pady=10, padx=10)
        self.conEntry = ctk.CTkEntry(self, placeholder_text="Enter Contractor Name", width=350)
        self.conEntry._set_appearance_mode("dark")
        self.conEntry.pack(side=ctk.LEFT, pady=10, padx=10)
        self.add_button = ctk.CTkButton(self, text="Add Contractor", command=self.add_contractor, fg_color="black", hover_color="gray")
        self.add_button._set_appearance_mode("dark")
        self.add_button.pack(side=ctk.LEFT, pady=10, padx=10)
        self.pack(fill=ctk.X, side=ctk.TOP)  # Ensures the frame is at the top and fills the width


    # Method to add a contractor
    def add_contractor(self):
        # Creating a contractor object
        contractor = Contractor(self.conEntry.get())

        # Adding the contractor to the database
        self.database.addContractor(contractor.getCN())
        self.conEntry.delete(0, ctk.END)


# Calf Entry Frame
class CalfEntryFrame(ctk.CTkFrame):

    # Constructor
    def __init__(self, parent, database):
        super().__init__(parent, height=100, width=150, border_color="black", border_width=2)

        # Getting the database object and contractors
        self.database = database
        contractors = self.database.getContractors()
        self._set_appearance_mode("dark")

        # Creating the widgets
        self.top_label = ctk.CTkLabel(self, text="Calf")
        self.top_label._set_appearance_mode("dark")
        self.top_label.pack(side=ctk.TOP, pady=10, padx=10)

        # Creating Calf info widgets
        self.con_select = ctk.CTkComboBox(self, width=130, values=contractors)
        self.con_select._set_appearance_mode("dark")
        self.con_select.pack(side=ctk.TOP, pady=10, padx=10)
        self.ear_tag_entry = ctk.CTkEntry(self, placeholder_text="Enter Ear Tag", width=130)
        self.ear_tag_entry._set_appearance_mode("dark")
        self.ear_tag_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.kick_entry = ctk.CTkComboBox(self, width=130, values=["Select Kick", "Yes", "No"])
        self.kick_entry._set_appearance_mode("dark")
        self.kick_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.speed_entry = ctk.CTkComboBox(self, width=130, values=["Select Speed", "Fast", "Normal", "Slow"])
        self.speed_entry._set_appearance_mode("dark")
        self.speed_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.direction_entry = ctk.CTkComboBox(self, width=130, values=["Select Direction", "Left", "Right", "Straight"])
        self.direction_entry._set_appearance_mode("dark")
        self.direction_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.add_button = ctk.CTkButton(self, text="Add Run", fg_color="black", hover_color="gray", width=130, command=self.add_calf)
        self.add_button._set_appearance_mode("dark")
        self.add_button.pack(side=ctk.TOP, pady=10, padx=10)
        self.pack(fill=ctk.X, side=ctk.TOP)

    # Method to add a calf
    def add_calf(self):
        # Creating a calf object
        calf = Calf(self.ear_tag_entry.get())
        calf.setKick(self.kick_entry.get())
        calf.setSpeed(self.speed_entry.get())
        calf.setDirection(self.direction_entry.get())

        # Adding the calf to the database
        self.database.addCalf(calf.getET(), self.con_select.get(), calf.getKick(), calf.getSpeed(), calf.getDirection())
        self.ear_tag_entry.delete(0, ctk.END)



# steer Entry Frame
class SteerEntryFrame(ctk.CTkFrame):

    # Constructor
    def __init__(self, parent, database):
        super().__init__(parent, height=100, width=150, border_color="black", border_width=2)

        # Getting the database object and contractors
        self.database = database
        contractors = self.database.getContractors()
        self._set_appearance_mode("dark")

        # Creating the widgets
        self.top_label = ctk.CTkLabel(self, text="Steer")
        self.top_label._set_appearance_mode("dark")
        self.top_label.pack(side=ctk.TOP, pady=10, padx=10)

        # Creating steer info widgets
        self.con_select = ctk.CTkComboBox(self, width=130, values=contractors)
        self.con_select._set_appearance_mode("dark")
        self.con_select.pack(side=ctk.TOP, pady=10, padx=10)
        self.ear_tag_entry = ctk.CTkEntry(self, placeholder_text="Enter Ear Tag", width=130)
        self.ear_tag_entry._set_appearance_mode("dark")
        self.ear_tag_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.stop_entry = ctk.CTkComboBox(self, width=130, values=["Select Stop", "Yes", "No"])
        self.stop_entry._set_appearance_mode("dark")
        self.stop_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.speed_entry = ctk.CTkComboBox(self, width=130, values=["Select Speed", "Fast", "Normal", "Slow"])
        self.speed_entry._set_appearance_mode("dark")
        self.speed_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.direction_entry = ctk.CTkComboBox(self, width=130,values=["Select Direction", "Left", "Right", "Straight"])
        self.direction_entry._set_appearance_mode("dark")
        self.direction_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.add_button = ctk.CTkButton(self, text="Add Run", fg_color="black", hover_color="gray", width=130,command=self.add_steer)
        self.add_button._set_appearance_mode("dark")
        self.add_button.pack(side=ctk.TOP, pady=10, padx=10)
        self.pack(fill=ctk.X, side=ctk.TOP)


    # Method to add a Steer
    def add_steer(self):
        # Creating a calf object
        steer = Steer(self.ear_tag_entry.get())
        steer.setStop(self.stop_entry.get())
        steer.setSpeed(self.speed_entry.get())
        steer.setDirection(self.direction_entry.get())

        # Adding the calf to the database
        self.database.addSteer(steer.getET(), self.con_select.get(), steer.getStop(), steer.getSpeed(), steer.getDirection())
        self.ear_tag_entry.delete(0, ctk.END)
        
        
        
# bull Entry Frame
class BullEntryFrame(ctk.CTkFrame):

    # Constructor
    def __init__(self, parent, database):
        super().__init__(parent, height=100, width=150, border_color="black", border_width=2)

        # Getting the database object and contractors
        self.database = database
        contractors = self.database.getContractors()
        self._set_appearance_mode("dark")

        # Creating the widgets
        self.top_label = ctk.CTkLabel(self, text="Bull")
        self.top_label._set_appearance_mode("dark")
        self.top_label.pack(side=ctk.TOP, pady=10, padx=10)

        # Creating bull info widgets
        self.con_select = ctk.CTkComboBox(self, width=130, values=contractors)
        self.con_select._set_appearance_mode("dark")
        self.con_select.pack(side=ctk.TOP, pady=10, padx=10)
        self.ear_tag_entry = ctk.CTkEntry(self, placeholder_text="Enter Ear Tag", width=130)
        self.ear_tag_entry._set_appearance_mode("dark")
        self.ear_tag_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.straight_entry = ctk.CTkComboBox(self, width=130, values=["Select straight", "Yes", "No"])
        self.straight_entry._set_appearance_mode("dark")
        self.straight_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.speed_entry = ctk.CTkComboBox(self, width=130, values=["Select Speed", "Fast", "Normal", "Slow"])
        self.speed_entry._set_appearance_mode("dark")
        self.speed_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.direction_entry = ctk.CTkComboBox(self, width=130,values=["Select Direction", "Left", "Right", "Straight"])
        self.direction_entry._set_appearance_mode("dark")
        self.direction_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.add_button = ctk.CTkButton(self, text="Add Run", fg_color="black", hover_color="gray", width=130,command=self.add_bull)
        self.add_button._set_appearance_mode("dark")
        self.add_button.pack(side=ctk.TOP, pady=10, padx=10)
        self.pack(fill=ctk.X, side=ctk.TOP)


    # Method to add a bull
    def add_bull(self):
        # Creating a calf object
        bull = Bull(self.ear_tag_entry.get())
        bull.setStraight(self.straight_entry.get())
        bull.setSpeed(self.speed_entry.get())
        bull.setDirection(self.direction_entry.get())

        # Adding the calf to the database
        self.database.addBull(bull.getET(), self.con_select.get(), bull.getStraight(), bull.getSpeed(), bull.getDirection())
        self.ear_tag_entry.delete(0, ctk.END)


# Bronc Entry Frame
class BroncEntryFrame(ctk.CTkFrame):

    # Constructor
    def __init__(self, parent, database):
        super().__init__(parent, height=100, width=150, border_color="black", border_width=2)

        # Getting the database object and contractors
        self.database = database
        contractors = self.database.getContractors()
        self._set_appearance_mode("dark")

        # Creating the widgets
        self.top_label = ctk.CTkLabel(self, text="Bronc")
        self.top_label._set_appearance_mode("dark")
        self.top_label.pack(side=ctk.TOP, pady=10, padx=10)

        # Creating bronc info widgets
        self.con_select = ctk.CTkComboBox(self, width=130, values=contractors)
        self.con_select._set_appearance_mode("dark")
        self.con_select.pack(side=ctk.TOP, pady=10, padx=10)
        self.ear_tag_entry = ctk.CTkEntry(self, placeholder_text="Enter Ear Tag", width=130)
        self.ear_tag_entry._set_appearance_mode("dark")
        self.ear_tag_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.flank_tag_entry = ctk.CTkEntry(self, placeholder_text="Enter Flank", width=130)
        self.flank_tag_entry._set_appearance_mode("dark")
        self.flank_tag_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.straight_entry = ctk.CTkComboBox(self, width=130, values=["Select straight", "Yes", "No"])
        self.straight_entry._set_appearance_mode("dark")
        self.straight_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.speed_entry = ctk.CTkComboBox(self, width=130, values=["Select Speed", "Fast", "Normal", "Slow"])
        self.speed_entry._set_appearance_mode("dark")
        self.speed_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.direction_entry = ctk.CTkComboBox(self, width=130,values=["Select Direction", "Left", "Right", "Straight"])
        self.direction_entry._set_appearance_mode("dark")
        self.direction_entry.pack(side=ctk.TOP, pady=10, padx=10)
        self.add_button = ctk.CTkButton(self, text="Add Run", fg_color="black", hover_color="gray", width=130,command=self.add_bronc)
        self.add_button._set_appearance_mode("dark")
        self.add_button.pack(side=ctk.TOP, pady=10, padx=10)
        self.pack(fill=ctk.X, side=ctk.TOP)


    # Method to add a bronc
    def add_bronc(self):
        # Creating a calf object
        bronc = Bronc(self.ear_tag_entry.get())
        bronc.setStraight(self.straight_entry.get())
        bronc.setSpeed(self.speed_entry.get())
        bronc.setDirection(self.direction_entry.get())
        bronc.setFlankTightness(self.flank_tag_entry.get())

        # Adding the calf to the database
        self.database.addBronc(bronc.getET(), self.con_select.get(), bronc.getStraight(), bronc.getSpeed(), bronc.getDirection(), bronc.getFlankTightness())
        self.ear_tag_entry.delete(0, ctk.END)


# Class to make the App
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        db = Database()
        self.geometry("600x450")  # Adjusted to accommodate side-by-side frames
        self.title("SecondRodeo")
        self._set_appearance_mode("dark")

        # Create frames
        self.con_frame = ContractorFrame(parent=self, database=db)
        self.cal_frame = CalfEntryFrame(parent=self, database=db)
        self.steer_frame = SteerEntryFrame(parent=self, database=db)
        self.bull_frame = BullEntryFrame(parent=self, database=db)
        self.bronc_frame = BroncEntryFrame(parent=self, database=db)

        # Pack contractor frame at the top
        self.con_frame.pack(side=ctk.TOP, fill=ctk.X)

        # Create a container frame to hold calf and steer frames side by side
        self.side_frame = ctk.CTkFrame(self)
        self.side_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        # Pack calf and steer frames side by side
        self.cal_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        self.steer_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        self.bull_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        self.bronc_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)


# Run the app
if __name__ == '__main__':
    app = App()
    app.mainloop()
