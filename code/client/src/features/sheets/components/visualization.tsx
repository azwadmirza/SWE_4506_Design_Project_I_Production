import "../assets/css/sheets.css";
import Header from "../components/header";
import ValueDisplay from "../components/value-display";
import { useSheets } from "../hooks/useSheets";
import Loader from "../../../partials/loader";
import { Provider } from "react-redux";
import { store } from "../../../contexts/file/store";
import { useAppSelector } from "../../../contexts/file/hooks";
import Charts from "../../visualization/components/charts";

const Visualization = () => {
  const file = useAppSelector((state) => state.file.file);
  const {
    currentCell,
    gridRows,
    viewValue,
    setViewValue,
    loading,
    onCellChange,
  } = useSheets();
  if (!loading) {
    return (
      <Provider store={store}>
        <div className="sheets">
          <Header filename={`${file !== null ? file : ""}`} />
          {currentCell !== "" && (
            <ValueDisplay
              currentCell={currentCell}
              value={viewValue}
              setValue={setViewValue}
            />
          )}
          <div className="render-cells">
            <h1>Visulation</h1>
            <Charts />
          </div>
        </div>
      </Provider>
    );
  } else {
    return <Loader />;
  }
};

export default Visualization;
