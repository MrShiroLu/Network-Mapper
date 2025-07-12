import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time
from .scanner import scan

class NetworkMapperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NetworkMapper")
        # Define colors first
        self.colors = {
            'bg': '#1e1e1e',
            'primary': '#007acc',
            'secondary': '#2d2d30',
            'accent': '#28a745',
            'text': '#ffffff',
            'border': '#3e3e42',
            'entry_bg': '#3c3c3c',
            'button_bg': '#007acc',
            'button_hover': '#005a9e',
            'error': '#f44336',
            'success': '#4caf50'
        }
        self.root.geometry("850x700")
        self.root.configure(bg=self.colors['bg'])
        # Scan state
        self.scanning = False
        self.scan_thread = None
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(
            title_frame, 
            text="NetworkMapper", 
            font=("Arial", 24, "bold"),
            fg=self.colors['primary'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Port Scanner Tool",
            font=("Arial", 12),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        subtitle_label.pack()
        
        # Input fields
        input_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Target input
        target_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        target_frame.pack(fill=tk.X, pady=(0, 10))
        
        target_label = tk.Label(
            target_frame,
            text="Target (IP/Hostname):",
            font=("Arial", 10, "bold"),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        target_label.pack(anchor=tk.W)
        
        self.target_entry = tk.Entry(
            target_frame,
            font=("Arial", 11),
            bg=self.colors['entry_bg'],
            fg=self.colors['text'],
            relief=tk.FLAT,
            bd=2,
            insertbackground=self.colors['text']
        )
        self.target_entry.pack(fill=tk.X, pady=(5, 0))        
        # Port input
        port_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        port_frame.pack(fill=tk.X, pady=(0, 10))
        
        port_label = tk.Label(
            port_frame,
            text="Ports (e.g., 80-1000 or 22,80,443):",
            font=("Arial", 10, "bold"),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        port_label.pack(anchor=tk.W)
        
        self.port_entry = tk.Entry(
            port_frame,
            font=("Arial", 11),
            bg=self.colors['entry_bg'],
            fg=self.colors['text'],
            relief=tk.FLAT,
            bd=2,
            insertbackground=self.colors['text']
        )
        self.port_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.scan_button = tk.Button(
            button_frame,
            text="Start Scan",
            font=("Arial", 12, "bold"),
            bg=self.colors['accent'],
            fg="white",
            relief=tk.FLAT,
            bd=0,
            padx=30,
            pady=10,
            command=self.start_scan
        )
        self.scan_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_button = tk.Button(
            button_frame,
            text="Stop Scan",
            font=("Arial", 12, "bold"),
            bg=self.colors['error'],
            fg="white",
            relief=tk.FLAT,
            bd=0,
            padx=30,
            pady=10,
            command=self.stop_scan,
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_button = tk.Button(
            button_frame,
            text="Clear Results",
            font=("Arial", 12),
            bg=self.colors['secondary'],
            fg=self.colors['text'],
            relief=tk.FLAT,
            bd=0,
            padx=30,
            pady=10,
            command=self.clear_results
        )
        self.clear_button.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress_var = tk.StringVar()
        
        progress_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        progress_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.progress_label = tk.Label(
            progress_frame,
            textvariable=self.progress_var,
            font=("Arial", 10),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        self.progress_label.pack()
        
        # Results
        results_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        results_label = tk.Label(
            results_frame,
            text="Scan Results:",
            font=("Arial", 12, "bold"),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        results_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Scrolled text widget
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            font=("Consolas", 10),
            bg=self.colors['entry_bg'],
            fg=self.colors['text'],
            relief=tk.FLAT,
            bd=2,
            wrap=tk.WORD,
            insertbackground=self.colors['text']
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg=self.colors['secondary'],
            fg=self.colors['text'],
            font=("Arial", 9)
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def start_scan(self):
        target = self.target_entry.get().strip()
        ports = self.port_entry.get().strip()
        
        if not target or not ports:
            messagebox.showerror("Error", "Please enter both target and ports!")
            return
        
        # Scan state
        self.scanning = True
        
        # Update UI
        self.scan_button.config(state=tk.DISABLED, text="Scanning...")
        self.stop_button.config(state=tk.NORMAL)
        self.progress_var.set("Scanning in progress...")
        self.status_var.set("Scanning...")
        self.results_text.delete(1.0, tk.END)
        
        # Start scan in a separate thread
        self.scan_thread = threading.Thread(target=self.perform_scan, args=(target, ports))
        self.scan_thread.daemon = True
        self.scan_thread.start()
        
    def perform_scan(self, target, ports):
        try:
            # Show banner
            self.results_text.insert(tk.END, "=" * 60 + "\n")
            self.results_text.insert(tk.END, "NetworkMapper Port Scanner\n")
            self.results_text.insert(tk.END, "=" * 60 + "\n\n")
            self.results_text.insert(tk.END, f"Target: {target}\n")
            self.results_text.insert(tk.END, f"Ports: {ports}\n")
            self.results_text.insert(tk.END, f"Start Time: {time.strftime('%H:%M:%S')}\n\n")
            self.results_text.insert(tk.END, "Scanning...\n\n")
            self.results_text.see(tk.END)
            
  
            # Call scanner and get results
            scan_results = scan(target, ports)
            
            # Check if scan was stopped
            if not self.scanning:
                return
            
            # Display results in GUI
            for result in scan_results:
                if not self.scanning:  # Check before displaying each result
                    break
                self.results_text.insert(tk.END, result + "\n")
                self.results_text.see(tk.END)
                self.root.update_idletasks()
            
            if self.scanning:  # Only show completion message if scan was not stopped
                
                # Update UI
                self.root.after(0, self.scan_completed)
            
        except Exception as e:
            error_msg = f"Error during scan: {str(e)}"
            self.root.after(0, lambda: self.show_error(error_msg))
    
    def stop_scan(self):
        if self.scanning:
            self.scanning = False
            self.progress_var.set("Scan stopped by user")
            self.status_var.set("Stopped")
            self.scan_button.config(state=tk.NORMAL, text="Start Scan")
            self.stop_button.config(state=tk.DISABLED)
            self.results_text.insert(tk.END, "\n[SCAN STOPPED BY USER]\n")
            self.results_text.see(tk.END)
    
    def scan_completed(self):
        self.scanning = False
        self.scan_button.config(state=tk.NORMAL, text="Start Scan")
        self.stop_button.config(state=tk.DISABLED)
        self.progress_var.set("Scan completed")
        self.status_var.set("Ready")
        self.results_text.see(tk.END)
    
    def show_error(self, error_msg):
        self.scanning = False
        self.scan_button.config(state=tk.NORMAL, text="Start Scan")
        self.stop_button.config(state=tk.DISABLED)
        self.progress_var.set("Scan failed")
        self.status_var.set("Error")
        messagebox.showerror("Scan Error", error_msg)
    
    def clear_results(self):
        self.results_text.delete(1.0, tk.END)
        self.progress_var.set("Ready to scan")
        self.status_var.set("Ready")

def main():
    root = tk.Tk()
    app = NetworkMapperGUI(root)
    root.mainloop()

