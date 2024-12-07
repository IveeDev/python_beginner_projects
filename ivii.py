# QUESTION = "question"
# OPTION = "option"
# ANSWER = "answer"
# # quiz = [
# #     {
# #         QUESTION: "What is the capital of France?",
# #         OPTION: ["A. Berlin", "B. Madrid", "C. Paris", "D. London"],
# #         ANSWER: "C"
# #     },
# #     {
# #         QUESTION: "Which planet is known as the Red Planet?",
# #         OPTION: ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
# #         ANSWER: "B"
# #     }
# # ]
# quiz = {
#     "History": [
#         {
#             QUESTION: "Who was the first President of the United States?",
#             OPTION: ["A. George Washington", "B. Abraham Lincoln", "C. Thomas Jefferson", "D. John Adams"],
#             ANSWER: "A"
#         },
#         {
#             QUESTION: "In which year did World War II end?",
#             OPTION: ["A. 1940", "B. 1945", "C. 1939", "D. 1950"],
#             ANSWER: "B"
#         },
#     ],
#     "Science": [
#         {
#             QUESTION: "Which planet is known as the Red Planet?",
#             OPTION: ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
#             ANSWER: "B"
#         },
#         {
#             QUESTION: "What is the chemical symbol for water?",
#             OPTION: ["A. H2O", "B. CO2", "C. O2", "D. NaCl"],
#             ANSWER: "A"
#         },
#     ]
# }
# for cat, questions in quiz.items():
#     print(cat, questions)

# # print("Question-data --------")
#     for i, question_data in enumerate(questions):
#         print(question_data[QUESTION])
#         print(question_data[OPTION])

# arr = [2, 7, 11, 15]


# def sum_arr(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 print(arr[i], arr[j])
#                 print(i, j)


# sum_arr(arr, 9)
for index, column in range(3):
    print(index, column)
