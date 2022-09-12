import os
import numpy as np
import tensorflow as tf

path = r"C:\Users\84386\Desktop\GIT\Deep-Learning-Approach-for-Surface-Defect-Detection\DATA2"

# Create folder
# for count in range(2, 6):
#     os.mkdir(f"{path}/kros{count}")
data_list = os.listdir(path)
test_ratio = 0.4

def main():
    for index in range(len(data_list)):
        file_basename_image = data_list[index]
        file_basename_label = data_list[index]
        image_path = os.path.join(path, file_basename_image)
        # print("a: ", image_path)
        label_path = os.path.join(path, file_basename_label)
        # print("b: ", label_path)
    example_lists = {os.path.basename(x[0]): x[2] for x in os.walk(path)}
    example_dirs = [x[1] for x in os.walk(path)][0]
    train_test_offset = np.floor(len(example_lists) * (1 - test_ratio))
    a = np.floor(len(example_lists))
    print('train_offset: ', example_lists)
    print("before: ", example_lists)
    for i in range(len(example_dirs)):
        example_dir = example_dirs[i]
        example_list = example_lists[example_dir]
        # 过滤label图片
        example_list = [item for item in example_list if "label" not in item]
        example_dirs.sort()
        print('after: ', example_list)
        if i < train_test_offset:
            for j in range(len(example_list)):
                example_image = example_dir + '/' + example_list[j]
                example_label = example_image.split(".")[0] + "_label.png"
                # 判断是否是正样本
                print("label",example_label)
                index = example_list[j].split(".")[0][-1]
                print("index",index)
        #         if index in positive_index[i]:
        #             Positive_examples_train.append([example_image, example_label])
        #         else:
        #             Negative_examples_train.append([example_image, example_label])
        # else:
        #     for j in range(len(example_list)):
        #         example_image = example_dir + '/' + example_list[j]
        #         example_label = example_image.split(".")[0] + "_label.png"
        #         index = example_list[j].split(".")[0][-1]
        #         if index in positive_index[i]:
        #             Positive_examples_valid.append([example_image, example_label])
        #         else:
        #             Negative_examples_valid.append([example_image, example_label])


if __name__ == '__main__':
    main();
