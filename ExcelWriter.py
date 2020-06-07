import xlsxwriter


class ExcelWriter:
    @staticmethod
    def append_excel_extension(file_name):
        # Add the excel extension if needed
        if not file_name.endswith(".xlsx"):
            file_name = file_name + ".xlsx"
        return file_name

    @staticmethod
    def write_to_excel_file(file_name, headers, data_list):
        workbook = xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet("Inventory")
        row = 0

        # Add Worksheet headers
        col_widths = []         # Track max column widths for 'auto resizing'
        col_formattings = []    # Keep track of specified column formatting

        for i in range(len(headers)):
            # Retrieve the header name and options
            header_name = headers[i]['name']
            column_format = workbook.add_format(headers[i]['format_options'])

            # Add for book keeping
            col_formattings.append(column_format)
            col_widths.append(len(header_name) + 5)

            # Set the desired width and header name
            worksheet.set_column(i, i, col_widths[i])
            worksheet.write(row, i, header_name)

        # Add the Worksheet data
        for data in data_list:
            row += 1
            for i in range(len(data)):
                data_len = len(str(data[i]))

                # Resize if necessary
                if data_len > col_widths[i]:
                    col_widths[i] = data_len
                    worksheet.set_column(i, i, col_widths[i])

                worksheet.write(row, i, data[i], col_formattings[i])

        workbook.close()

    # def write_to_excel_file(file_path, excel_options):
    #     num_rows = len(excel_options['data'])  # includes the header
    #     num_columns = len(excel_options['columns']) - 1
    #
    #     # Create a new excel worksheet
    #     workbook = xlsxwriter.Workbook(file_path)
    #     worksheet = workbook.add_worksheet("Inventory")
    #
    #     worksheet.add_table(first_row=0,
    #                         first_col=0,
    #                         last_row=num_rows,
    #                         last_col=num_columns,
    #                         options=excel_options)
    #     workbook.close()
