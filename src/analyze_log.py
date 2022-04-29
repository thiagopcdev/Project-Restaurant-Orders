import src.helper.analyze_functions as af


def analyze_log(path_to_file):
    try:
        most_req_by_maria = af.get_most_requested_dish(path_to_file, 'maria')
        arnaldo_hamburguer_qnt = af.get_order_quantity_by(
            path_to_file,
            'arnaldo',
            'hamburguer'
        )
        never_asked_by_joao = af.get_never_asked_by(path_to_file, 'joao')
        days_joao_never_went = af.get_days_client_never_went(
            path_to_file,
            'joao'
        )

        with open('data/mkt_campaign.txt', mode='w') as file:
            lines = [
                f'{most_req_by_maria}\n',
                f'{arnaldo_hamburguer_qnt}\n',
                f'{never_asked_by_joao}\n',
                f'{days_joao_never_went}\n'
            ]

            for line in lines:
                file.write(line)
    except FileNotFoundError:
        if 'csv' not in path_to_file:
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


analyze_log('data/orders_1.csv')
