"""
    和文件相关
    如读写文件。
"""
import pickle
from scipy.io import loadmat
from scipy.io import savemat


class CoreFile:

    # 保存文件
    @staticmethod
    def write_to_pkl(_path, _data):
        with open(_path, "wb") as f:
            pickle.dump(_data, f)
        pass

    # 读取文件
    @staticmethod
    def read_from_pkl(_path):
        with open(_path, "rb") as f:
            return pickle.load(f)
        pass

    # txt写
    @staticmethod
    def write_to_txt(_path, _data):
        with open(_path, "w") as f:
            f.write(_data)
        pass

    # txt读
    @staticmethod
    def read_from_txt(_path):
        with open(_path, "r") as f:
            return f.read()
        pass

    # mat写
    @staticmethod
    def write_to_mat(_path, _dict_data):
        if not isinstance(_dict_data, dict):
            raise TypeError
        savemat(_path, _dict_data)

    # mat读
    @staticmethod
    def read_all_from_mat(_path,):
        return loadmat(_path)

    @staticmethod
    def read_col_from_mat(_path, _col):
        return loadmat(_path)[_col]


if __name__ == "__main__":

    base_path = "../data/CoreFile/"
    pkl_path = base_path + "test.pkl"
    txt_path = base_path + "test.txt"
    mat_path = base_path + "test.mat"

    # pkl
    data = {"a": "aaa",
            "b": "bbb"}
    CoreFile.write_to_pkl(pkl_path, data)
    print(CoreFile.read_from_pkl(pkl_path))

    # txt
    data = "1234"
    CoreFile.write_to_txt(txt_path, data)
    print(CoreFile.read_from_txt(txt_path))

    # mat
    col_a = "data_a"
    col_b = "data_b"
    data_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data_b = [[2, 2, 3], [5, 5, 6], [8, 8, 9]]
    data = {col_a: data_a, col_b: data_b}
    CoreFile.write_to_mat(mat_path, data)
    print(CoreFile.read_all_from_mat(mat_path))
    print(CoreFile.read_col_from_mat(mat_path, col_a))
