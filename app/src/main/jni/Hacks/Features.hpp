namespace Features {
	//Lotto Sets 10k
	bool isLottoSets10k = false;
	bool updateToggle_LottoSets10k = false;
	bool isToggle_LottoSets10kFirstCall = true;
	void Toggle_LottoSets10k(bool value) {
        if (!isToggle_LottoSets10kFirstCall) {
            isLottoSets10k = value;
            updateToggle_LottoSets10k = true;
        } else {
            isToggle_LottoSets10kFirstCall = false;
        }
    }
}