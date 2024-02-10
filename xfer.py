import streamlit as st

# function that takes in number of seconds and returns a string of the time in days, hours, minutes, and seconds
def convert_seconds(seconds):
    days = int(seconds // 86400)
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)

    if days > 0:
        return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    elif hours > 0:
        return f"{hours} hours, {minutes} minutes, {seconds} seconds"
    elif minutes > 0:
        return f"{minutes} minutes, {seconds} seconds"
    else:
        return f"{seconds} seconds"

st.title("File Transfer Time Calculator")
st.header("Calculate data transfer speed")
data_amt = st.number_input("Amount of data to be transferred (in GB)", min_value=0.1, value=1.0)

#link_speed = st.number_input("Link speed in Mbps", min_value=None)

link_speed = st.slider("Link speed (in Mbps)", min_value=1, max_value=10000, value=100)

#link_speed = st.selectbox('Select link speed (in Mbps)',
#    ('10', '100', '1000', '10000'))

transfer_speed =  (data_amt*1024) / (0.125 * float(link_speed))
if transfer_speed > 1:
    int(transfer_speed)
else:
    round(transfer_speed, 2)

str_conv = convert_seconds(transfer_speed)

# Display transfer speed
st.write(f'Time to transfer {data_amt} GB of data at {link_speed} Mbps is {str_conv}' ) 
