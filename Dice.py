import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result = []

for i in range(0, 1000):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    dice_result.append(d1+d2)

mean = sum(dice_result)/len(dice_result)

standard_deviation = statistics.stdev(dice_result)

median = statistics.median(dice_result)

mode = statistics.mode(dice_result)
#
#print("Mean:", mean)
#print("median:", median)
#print("Mode:", mode)
#print("standard_deviation:", standard_deviation)

sd1_start, sd1_end = mean - standard_deviation, mean + standard_deviation

sd2_start, sd2_end = mean - (standard_deviation *
                             2), mean + (standard_deviation * 2)
sd3_start, sd3_end = mean - (standard_deviation *
                             3), mean + (standard_deviation * 3)


fig = ff.create_distplot([dice_result], ["Result"], show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="Mean"))

fig.add_trace(go.Scatter(x=[sd1_start, sd1_start], y=[
              0, 0.17], mode="lines", name="Standard Deviation 1"))

fig.add_trace(go.Scatter(x=[sd1_end, sd1_end], y=[
              0, 0.17], mode="lines", name="Standard Deviation 1"))

fig.add_trace(go.Scatter(x=[sd2_start, sd2_start], y=[
              0, 0.17], mode="lines", name="Standard Deviation 2"))

fig.add_trace(go.Scatter(x=[sd2_end, sd2_end], y=[
              0, 0.17], mode="lines", name="Standard Deviation 2"))

fig.add_trace(go.Scatter(x=[sd3_start, sd3_start], y=[
              0, 0.17], mode="lines", name="Standard Deviation 3"))

fig.add_trace(go.Scatter(x=[sd3_end, sd3_end], y=[
              0, 0.17], mode="lines", name="Standard Deviation 3"))

# fig.show()

data_sd1 = [result for result in dice_result if result >
            sd1_start and result < sd1_end]

data_sd2 = [result for result in dice_result if result >
            sd2_start and result < sd2_end]

data_sd3 = [result for result in dice_result if result >
            sd3_start and result < sd3_end]

#print("standard_deviation 01 data:", data_sd1)
#print("standard_deviation 02 data:", data_sd2)
#print("standard_deviation 03 data:", data_sd3)

print("{}% of data lies within first standard deviation".format(
    len(data_sd1) * 100.0/len(dice_result)))

print("{}% of data lies within second standard deviation".format(
    len(data_sd2) * 100.0/len(dice_result)))

print("{}% of data lies within third standard deviation".format(
    len(data_sd3) * 100.0/len(dice_result)))
