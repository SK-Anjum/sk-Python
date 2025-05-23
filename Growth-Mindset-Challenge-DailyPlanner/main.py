import streamlit as st
from datetime import datetime, time
import json
import os

DATA_FILE = "planner_tasks.json"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            tasks = json.load(f)
            # Convert time strings back to time objects
            for task in tasks:
                task["time"] = datetime.strptime(task["time"], "%H:%M:%S").time()
            return tasks
    return []

# Function to save tasks to file
def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump([
            {
                "task": t["task"],
                "time": t["time"].strftime("%H:%M:%S"),
                "completed": t["completed"]
            }
            for t in st.session_state.planner_tasks
        ], f, indent=2)

# Initialize session state
if "planner_tasks" not in st.session_state:
    st.session_state.planner_tasks = load_tasks()

st.title("🗓️ Daily Planner")

# Sidebar for adding tasks
st.sidebar.header("➕ Add New Task")

task_desc = st.sidebar.text_input("Task Description", placeholder="e.g., Team meeting")
task_time = st.sidebar.time_input("Scheduled Time", value=time(9, 0))

if st.sidebar.button("Add Task"):
    if task_desc.strip():
        st.session_state.planner_tasks.append({
            "task": task_desc,
            "time": task_time,
            "completed": False
        })
        save_tasks()
        st.success("Task added to your planner! ✅")
    else:
        st.warning("Task description cannot be empty!")

# Display tasks grouped by time
st.subheader("🕒 Today's Schedule")

if not st.session_state.planner_tasks:
    st.info("No tasks scheduled yet. Add a task using the sidebar.")
else:
    sorted_tasks = sorted(st.session_state.planner_tasks, key=lambda x: x["time"])
    for index, task in enumerate(sorted_tasks):
        col1, col2, col3 = st.columns([0.65, 0.2, 0.15])

        completed = col1.checkbox(f"{task['time'].strftime('%H:%M')} - {task['task']}",
                                  task["completed"],
                                  key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.planner_tasks[index]["completed"] = completed
            save_tasks()

        if col2.button("✏ Edit", key=f"edit_{index}"):
            with st.form(key=f"form_{index}"):
                new_desc = st.text_input("Update Task", task["task"])
                new_time = st.time_input("Update Time", task["time"])
                submitted = st.form_submit_button("Save")
                if submitted:
                    st.session_state.planner_tasks[index]["task"] = new_desc
                    st.session_state.planner_tasks[index]["time"] = new_time
                    save_tasks()
                    st.rerun()

        if col3.button("❌", key=f"delete_{index}"):
            del st.session_state.planner_tasks[index]
            save_tasks()
            st.rerun()

# Clear all tasks
if st.button("🗑 Clear All"):
    st.session_state.planner_tasks = []
    save_tasks()
    st.success("All tasks cleared!")

st.markdown("---")
st.caption("🧠 Plan your day effectively with the Daily Planner App!")
