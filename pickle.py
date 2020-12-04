import pickle
import numpy as np
#
# a = [1,2,3]
# b = (3,4,5)
#
# with open("star.pik", "wb") as f:
#     pickle.dump(a, f)
#     pickle.dump(b, f)
#
# with open("star.pik", "rb") as f:
#     x = pickle.load(f)
#     y = pickle.load(f)

xx = np.array([1,2,3,4,5,6,7,8,9,10])
np.save("numpyStyle.npy", xx)
type(xx)
