{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "489b2d19-1a7c-4d24-b584-9834d8e06d78",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "from time import strftime   #only import the strftime from the whole module \n",
    "\n",
    "from tkinter import Label, Tk  #Only Import the two functions from the module, The lable and the Tk\n",
    "                               #the label functions is used to implement the content box where we can place the images and the text.\n",
    "                               #Tk, the reason why we're importing the Tk module is because, of creating the main window.\n",
    "\n",
    "\n",
    "# Window config for clock \n",
    "window = Tk() #Storing the Tk in the Window Variable\n",
    "window.title (\"Digital Clock\") \n",
    "window.geometry(\"200x80\")\n",
    "window.configure(bg = \"black\" )\n",
    "window.resizable(False, False) # this means it cannot be resizable \n",
    "\n",
    "#Label config\n",
    "\n",
    "Clock_label = Label (window, bg= \"black\", fg= \"white\", font= (\"Time\", 20, 'bold'), relief= 'flat') #the relief argument is fir the decorative boarder_\n",
    "Clock_label.place(x= 20, y= 20)\n",
    "\n",
    "\n",
    "# Creating  function of the label we created to update every 80 milisecond  \n",
    "\n",
    "def updating_label():\n",
    "    current_time = strftime('%H: %M: %S') #hours, Minutes, and second modules respectively\n",
    "    Clock_label.configure(text = current_time)\n",
    "    Clock_label.after(80, updating_label)\n",
    "\n",
    "updating_label() # We call this function for updating our digital clock\n",
    "window.mainloop() # This is for perventing the windows from Existing Immediatery \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4c2d2a5-c143-4577-970f-3d3f37e7ccac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2b0f40a-fcdd-44a8-b396-948c822e74b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
