"""Get winners"""


class GetWinners:
    """Get Winners."""

    def removeDuplicateWinners(self, list_winners):
        """Remove duplicate winners."""
        reply_winners = list_winners[:]
        for reply_winner in reply_winners:
            num_repeated = 0
            for winner in list_winners:
                if winner['user_id'] == reply_winner['user_id']:
                    num_repeated += 1
                    if num_repeated > 1:
                        if winner['value_difference'] <= reply_winner['value_difference']:
                            if reply_winner in list_winners:
                                list_winners.remove(reply_winner)
                                break
                        else:
                            if winner in list_winners:
                                list_winners.remove(winner)
                                break
        return list_winners

    def chooseWinners(self, bets, final_value, range):
        """choose winners"""
        winners = []
        for bet in bets:
            if final_value == bet['bet_value']:
                winners.append(bet)

        if len(winners) == 0:
            validated_winners = []
            aux_winners = []
            validated_winners.append(final_value)
            for bet in bets:
                if bet['bet_value'] >= final_value - range and bet['bet_value'] <= final_value + range:
                    bet['value_difference'] = abs(final_value - bet['bet_value'])
                    winners.append(bet)

            for winner in winners:
                if validated_winners[-1] == winner['value_difference']:
                    validated_winners.append(winner['value_difference'])
                    aux_winners.append(winner)
                elif winner['value_difference'] < validated_winners[-1]:
                    validated_winners = []
                    aux_winners = []
                    validated_winners.append(winner['value_difference'])
                    aux_winners.append(winner)

            winners = self.removeDuplicateWinners(aux_winners)
            closest_final_value = self.closestFinalValue(bets, winners, final_value, range)

            result = {
                'winners': winners,
                'closest_final_value': closest_final_value,
            }

        return result

    def closestFinalValue(self, bets, list_winners, final_value, range):
        """closest final value"""
        winners = []
        list_aux = []
        reply_winners = bets[:]
        for bet in reply_winners:
            for winner in list_winners:
                if winner['user_id'] == bet['user_id']:
                    bets.remove(bet)
                    break

        for bet in bets:
            bet['value_difference'] = abs(final_value - bet['bet_value'])
            winners.append(bet)
        winners.sort(key=lambda x: x['value_difference'])

        winners = self.removeDuplicateWinners(winners)

        for winner in winners:
            if len(list_aux) == 0:
                list_aux.append([winner])
            elif list_aux[-1][0]['value_difference'] == winner['value_difference']:
                list_aux[-1].append(winner)
            else:
                list_aux.append([winner])

        return list_aux