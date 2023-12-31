import { Navbar, Container, Nav, Dropdown} from "react-bootstrap";
import { useDropDown } from "../hooks/useDropDown";
import FileInput from "../../../partials/fileInput";
import { useAppSelector} from "../../../contexts/file/hooks";

type HeaderProps = {
  filename: string;
};

const Header = ({ filename }: HeaderProps) => {
  const jsonData = useAppSelector((state)=> state.file.data)
  const { showFileDropdown,
    toggleDropdown,
    showFileUpload,
    setShowFileUpload } = useDropDown();
    


    const handleSave = () => {
      console.log("Began Saving");
      console.log(jsonData);
    };

  return (
    <Navbar className="header fixed-top" variant="dark" expand="lg">
      <Container
        fluid
        className="navbarContents px-0 px-lg-5 d-flex justify-content-between"
      >
        <Navbar.Brand className="px-2">{filename}</Navbar.Brand>
          <Nav
            className="me-auto my-2 my-lg-0 px-2"
            style={{ maxHeight: "150px" }}
            navbarScroll
          >
            <div className="option" onClick={() => toggleDropdown("file")}>
              File
              <FileInput showFileInput={showFileUpload} setShowFileInput={setShowFileUpload}/>
              {showFileDropdown && (
                <Dropdown
                  show={showFileDropdown}
                  onClick={() => toggleDropdown("file")}
                >
                  <Dropdown.Menu>
                    <Dropdown.Item onClick={()=>{
                      setShowFileUpload(!showFileUpload);
                    }}>Open</Dropdown.Item>
                    <Dropdown.Item onClick={handleSave}>Save</Dropdown.Item>
                  </Dropdown.Menu>
                </Dropdown>
              )}
            </div>
            <div className="option">Format</div>
          </Nav>
      </Container>
    </Navbar>
  );
};

export default Header;
