import tkinter as tk
from tkinter import ttk

class TVEducationalCampaignTool:
    def __init__(self, master):
        self.master = master
        master.title("TV Educational Campaign Tool")

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Widgets
        self.show_label = ttk.Label(self.master, text="TV Show:")
        self.show_entry = ttk.Entry(self.master)

        self.campaign_label = ttk.Label(self.master, text="Campaign Title:")
        self.campaign_entry = ttk.Entry(self.master)

        # Buttons
        self.create_campaign_button = ttk.Button(self.master, text="Create Campaign", command=self.create_campaign)
        self.view_campaigns_button = ttk.Button(self.master, text="View Campaigns", command=self.view_campaigns)

        # Layout
        self.show_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.show_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.campaign_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.campaign_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.create_campaign_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.view_campaigns_button.grid(row=3, column=0, columnspan=2, pady=10)

    def create_campaign(self):
        show_name = self.show_entry.get()
        campaign_title = self.campaign_entry.get()

        if show_name and campaign_title:
            # Perform actions to create and manage the educational campaign
            # For demonstration purposes, you can print the details
            print(f"Created Campaign: {campaign_title} for {show_name}")
        else:
            print("Please enter both TV Show and Campaign Title.")

    def view_campaigns(self):
        # Perform actions to display and manage existing campaigns
        # For demonstration purposes, you can print a message
        print("Viewing existing campaigns.")

if __name__ == '__main__':
    root = tk.Tk()
    app = TVEducationalCampaignTool(root)
    root.mainloop()
