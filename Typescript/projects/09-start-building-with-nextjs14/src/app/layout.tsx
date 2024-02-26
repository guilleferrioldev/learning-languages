import type { Metadata } from "next";
import "./globals.css";
import { montserrat } from "./fonts";
import NavLinks  from './nav-links'

export const metadata: Metadata = {
  title: "Learning Next",
  description: "Learning Next",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>): JSX.Element {
  return (
    <html lang="en">
      <body className={montserrat.className}>
        <NavLinks />
        {children} 
      </body>
    </html>
  );
}
