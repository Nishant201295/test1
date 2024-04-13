import streamlit as st
import pandas as pd
import datetime

class Nse:
    def __init__(self):
        self.stop = False
        self.first_run = True
        self.seconds = 60
        self.time_difference_factor = 10
        self.warn_late_update = True
        self.save_oc = False
        self.update = False
        self.auto_stop = False
        self.notifications = True
        self.round_factor = 1
        self.sp = 0
        self.expiry_date = "2024-04-13"
        self.icon_ico_path = ""
        self.load_nse_icon = False
        self.previous_date = None
        self.previous_time = None
        self.toaster = None
        self.index = "NIFTY"
        self.option_mode = "Index"
        self.max_call_oi = 0
        self.max_call_oi_sp = 0
        self.max_put_oi = 0
        self.max_put_oi_sp = 0
        self.max_call_oi_2 = 0
        self.max_call_oi_sp_2 = 0
        self.max_put_oi_2 = 0
        self.max_put_oi_sp_2 = 0
        self.put_call_ratio = 0
        self.call_sum = 0
        self.put_sum = 0
        self.difference = 0
        self.call_boundary = 0
        self.put_boundary = 0
        self.call_itm = 0
        self.put_itm = 0
        self.str_current_time = ""
        self.points = 0

    def set_values(self):
        st.write("Setting values...")  # Placeholder for setting values

    def get_dataframe(self):
        # Placeholder for getting data from dataframe
        return pd.DataFrame(), str(datetime.datetime.now()), 0

    def check_for_updates(self):
        # Placeholder for checking updates
        st.write("Checking for updates...")

    def main(self):
        if self.stop:
            return

        entire_oc, current_time, self.points = self.get_dataframe()

        self.str_current_time = current_time.split(" ")[1]
        try:
            current_date = datetime.datetime.strptime(current_time.split(" ")[0], '%Y-%m-%d').date()
            current_time = datetime.datetime.strptime(current_time.split(" ")[1], '%H:%M:%S').time()
        except ValueError:
            st.error("Error: Failed to parse current time.")
            return

        if self.first_run:
            self.previous_date = current_date
            self.previous_time = current_time
        elif current_date > self.previous_date:
            self.previous_date = current_date
            self.previous_time = current_time
        elif current_date == self.previous_date:
            if current_time > self.previous_time:
                time_difference = 0
                if current_time.hour > self.previous_time.hour:
                    time_difference = (60 - self.previous_time.minute) + current_time.minute + \
                                      ((60 - self.previous_time.second) + current_time.second) / 60
                elif current_time.hour == self.previous_time.hour:
                    time_difference = current_time.minute - self.previous_time.minute + \
                                      (current_time.second - self.previous_time.second) / 60
                if time_difference >= self.time_difference_factor and self.warn_late_update:
                    st.warning(f"The data from the server was last updated about {int(time_difference)} minutes ago.")
                self.previous_time = current_time
            else:
                return

        call_oi_list = []
        for i in range(len(entire_oc)):
            int_call_oi = int(entire_oc.iloc[i, [0]][0])
            call_oi_list.append(int_call_oi)
        call_oi_index = call_oi_list.index(max(call_oi_list))
        self.max_call_oi = round(max(call_oi_list) / self.round_factor, 1)
        self.max_call_oi_sp = float(entire_oc.iloc[call_oi_index]['Strike Price'])

        put_oi_list = []
        for i in range(len(entire_oc)):
            int_put_oi = int(entire_oc.iloc[i, [20]][0])
            put_oi_list.append(int_put_oi)
        put_oi_index = put_oi_list.index(max(put_oi_list))
        self.max_put_oi = round(max(put_oi_list) / self.round_factor, 1)
        self.max_put_oi_sp = float(entire_oc.iloc[put_oi_index]['Strike Price'])

        sp_range_list = []
        for i in range(put_oi_index, call_oi_index + 1):
            sp_range_list.append(float(entire_oc.iloc[i]['Strike Price']))

        self.max_call_oi_2 = self.max_call_oi
        self.max_call_oi_sp_2 = self.max_call_oi_sp
        self.max_put_oi_2 = self.max_put_oi
        self.max_put_oi_sp_2 = self.max_put_oi_sp
        if len(sp_range_list) == 2:
            self.max_call_oi_2 = round((entire_oc[entire_oc['Strike Price'] == self.max_put_oi_sp].iloc[0, 0]) /
                                       self.round_factor, 1)
            self.max_call_oi_sp_2 = self.max_put_oi_sp
            self.max_put_oi_2 = round((entire_oc[entire_oc['Strike Price'] == self.max_call_oi_sp].iloc[0, 20]) /
                                      self.round_factor, 1)
            self.max_put_oi_sp_2 = self.max_call_oi_sp
        else:
            call_oi_list_2 = []
            for i in range(put_oi_index, call_oi_index):
                int_call_oi_2 = int(entire_oc.iloc[i, [0]][0])
                call_oi_list_2.append(int_call_oi_2)
            call_oi_index_2 = put_oi_index + call_oi_list_2.index(max(call_oi_list_2))
            self.max_call_oi_2 = round(max(call_oi_list_2) / self.round_factor, 1)
            self.max_call_oi_sp_2 = float(entire_oc.iloc[call_oi_index_2]['Strike Price'])

            put_oi_list_2 = []
            for i in range(put_oi_index + 1, call_oi_index + 1):
                int_put_oi_2 = int(entire_oc.iloc[i, [20]][0])
                put_oi_list_2.append(int_put_oi_2)
            put_oi_index_2 = put_oi_index + 1 + put_oi_list_2.index(max(put_oi_list_2))
            self.max_put_oi_2 = round(max(put_oi_list_2) / self.round_factor, 1)
            self.max_put_oi_sp_2 = float(entire_oc.iloc[put_oi_index_2]['Strike Price'])

        total_call_oi = sum(call_oi_list)
        total_put_oi = sum(put_oi_list)
        self.put_call_ratio = round(total_put_oi / total_call_oi, 2)

        try:
            index = int(entire_oc[entire_oc['Strike Price'] == self.sp].index.tolist()[0])
        except IndexError:
            st.error("Incorrect Strike Price. Please enter correct Strike Price.")
            return

        a = entire_oc[['Change in Open Interest']][entire_oc['Strike Price'] == self.sp]
        b1 = a.iloc[:, 0]
        c1 = int(b1.get(index))
        b2 = entire_oc.iloc[:, 1]
        c2 = int(b2.get((index + 1), 'Change in Open Interest'))
        b3 = entire_oc.iloc[:, 1]
        c3 = int(b3.get((index + 2), 'Change in Open Interest'))
        if isinstance(c2, str):
            c2 = 0
        if isinstance(c3, str):
            c3 = 0
        self.call_sum = round((c1 + c2 + c3) / self.round_factor, 1)
        if self.call_sum == -0:
            self.call_sum = 0.0
        self.call_boundary = round(c3 / self.round_factor, 1)

        o1 = a.iloc[:, 1]
        p1 = int(o1.get(index))
        o2 = entire_oc.iloc[:, 19]
        p2 = int(o2.get((index + 1), 'Change in Open Interest'))
        p3 = int(o2.get((index + 2), 'Change in Open Interest'))
        if isinstance(p2, str):
            p2 = 0
        if isinstance(p3, str):
            p3 = 0
        self.put_sum = round((p1 + p2 + p3) / self.round_factor, 1)
        self.put_boundary = round(p1 / self.round_factor, 1)
        self.difference = round(self.call_sum - self.put_sum, 1)
        if self.p5 == 0:
            self.call_itm = 0.0
        else:
            self.call_itm = round(self.p4 / self.p5, 1)
            if self.call_itm == -0:
                self.call_itm = 0.0
        if isinstance(self.p6, str):
            self.p6 = 0
        if isinstance(self.p7, str):
            self.p7 = 0
        if self.p7 == 0:
            self.put_itm = 0.0
        else:
            self.put_itm = round(self.p6 / self.p7, 1)
            if self.put_itm == -0:
                self.put_itm = 0.0

        self.set_values()

        if self.save_oc:
            try:
                entire_oc.to_csv(
                    f"NSE-OCA-{self.index if self.option_mode == 'Index' else self.stock}-{self.expiry_date}-Full.csv",
                    index=False)
            except PermissionError:
                st.error("Failed to access NSE-OCA file due to permission denied.")
            except Exception as e:
                st.error(f"An error occurred while exporting data: {e}")

        if self.first_run:
            if self.update:
                self.check_for_updates()
            self.first_run = False
        if self.str_current_time == '15:30:00' and not self.stop and self.auto_stop \
                and self.previous_date == datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d"),
                                                                     "%Y-%m-%d").date():
            self.stop = True
            st.warning("Retrieving new data has been stopped.")
            return


def main():
    nse = Nse()
    nse.main()

if __name__ == '__main__':
    main()
